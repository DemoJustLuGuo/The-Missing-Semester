import os
import re
import pytz
import logging
from datetime import datetime, timedelta

try:
    START_DATE = datetime.fromisoformat(os.environ['START_DATE']).replace(tzinfo=pytz.UTC)
except KeyError:
    raise ValueError("Environment variable 'START_DATE' is not set.")
try:
    END_DATE = datetime.fromisoformat(os.environ['END_DATE']).replace(tzinfo=pytz.UTC)
except KeyError:
    raise ValueError("Environment variable 'END_DATE' is not set.")
DEFAULT_TIMEZONE = 'Asia/Shanghai'
README_FILE = 'README.md'
FILE_SUFFIX = os.environ.get('FILE_SUFFIX', '.md')
FIELD_NAME = os.environ.get('FIELD_NAME', 'Name')
CONTENT_START_MARKER = "<!-- Content_START -->"
CONTENT_END_MARKER = "<!-- Content_END -->"
TABLE_START_MARKER = "<!-- START_COMMIT_TABLE -->"
TABLE_END_MARKER = "<!-- END_COMMIT_TABLE -->"
MAX_MISS_TIMES = 5

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_date_range():
    return [START_DATE + timedelta(days=x) for x in range((END_DATE - START_DATE).days + 1)]

def get_user_timezone(file_content):
    yaml_match = re.search(r'---\s*\ntimezone:\s*(\S+)\s*\n---', file_content)
    if yaml_match:
        try:
            return pytz.timezone(yaml_match.group(1))
        except pytz.exceptions.UnknownTimeZoneError:
            logging.warning(
                f"Unknown timezone: {yaml_match.group(1)}. Using default {DEFAULT_TIMEZONE}.")
    return pytz.timezone(DEFAULT_TIMEZONE)

def get_user_study_status(nickname):
    user_status = {}
    file_name = f"{nickname}{FILE_SUFFIX}"
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
        user_tz = get_user_timezone(file_content)
        logging.info(
            f"File content length for {nickname}: {len(file_content)} user_tz: {user_tz}")
        current_date = datetime.now(user_tz).replace(
            hour=0, minute=0, second=0, microsecond=0)  # - timedelta(days=1)

        for date in get_date_range():
            if date.day == current_date.day:
                user_status[date] = "✅" if check_md_content(
                    file_content, date, pytz.UTC) else " "
            elif date > current_date:
                user_status[date] = " "
            else:
                user_status[date] = "✅" if check_md_content(
                    file_content, date, pytz.UTC) else "⭕️"

        logging.info(f"Successfully processed file for user: {nickname}")
    except FileNotFoundError:
        logging.error(f"Error: Could not find file {file_name}")
        user_status = {date: "⭕️" for date in get_date_range()}
    except Exception as e:
        logging.error(
            f"Unexpected error processing file for {nickname}: {str(e)}")
        user_status = {date: "⭕️" for date in get_date_range()}
    return user_status

def check_md_content(file_content, date, user_tz):
    try:
        content = extract_content_between_markers(file_content)
        local_date = date.astimezone(user_tz).replace(
            hour=0, minute=0, second=0, microsecond=0)
        
        # 查找日期
        current_date_matches = find_date_in_content(content, local_date)
        
        if current_date_matches:
            # 获取日期内容
            date_content = get_content_for_date(content, current_date_matches[0].end())
            
            # 如果没有内容，返回 0
            if not date_content.strip():  # 如果内容为空
                logging.info(f"No content found for {local_date.strftime('%Y-%m-%d')}")
                return 0  # 0表示没有内容
            
            # 处理空白字符，保留必要格式
            date_content = re.sub(r'\s{2,}', ' ', date_content).strip()  # 只去除多余空格，保留格式
            logging.info(f"Content length for {local_date.strftime('%Y-%m-%d')}: {len(date_content)}")
            
            return len(date_content) > 10
        else:
            logging.info(f"No match found for date {local_date.strftime('%Y-%m-%d')}")
            return False
    except Exception as e:
        logging.error(f"Error in check_md_content: {str(e)}")
        return False
    
def extract_content_between_markers(file_content):
    start_index = file_content.find(CONTENT_START_MARKER)
    end_index = file_content.find(CONTENT_END_MARKER)
    if start_index == -1 or end_index == -1:
        logging.warning("Content_START_MARKER markers not found in the file")
        return ""
    return file_content[start_index + len(CONTENT_START_MARKER):end_index].strip()

def find_date_in_content(content, local_date):
    # 定义日期的多个可能格式
    date_patterns = [
        r'###\s*' + local_date.strftime("%Y-%m.%d"),
        r'###\s*' + local_date.strftime("%Y.%m.%d").replace('.0', '.'),
        r'###\s*' + local_date.strftime("%m.%d").lstrip('0').replace('.0', '.'),
        r'###\s*' + local_date.strftime("%Y/%m/%d"),
        r'###\s*' + local_date.strftime("%m/%d").lstrip('0').replace('/0', '/'),
        r'###\s*' + local_date.strftime("%m.%d").zfill(5),
    ]
    combined_pattern = '|'.join(date_patterns)
    
    # 使用 findall 获取所有匹配的日期位置
    return [match for match in re.finditer(combined_pattern, content)]

def get_content_for_date(content, start_pos):
    # 获取下一个日期的模式
    next_date_pattern = r'###\s*(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}|\d{2}\.\d{2}|\d{4}/\d{2}/\d{2}|\d{4}\.\d{2}\.\d{2})'
    next_date_match = re.search(next_date_pattern, content[start_pos:])
    
    # 如果找到了下一个日期，返回当前日期和下一个日期之间的内容
    if next_date_match:
        # 返回当前日期到下一个日期之间的内容，排除掉日期行本身
        return content[start_pos:start_pos + next_date_match.start()].strip()
    return content[start_pos:]  # 如果没有下一个日期，返回剩余内容

def generate_user_row(user):
    user_status = get_user_study_status(user)
    with open(f"{user}{FILE_SUFFIX}", 'r', encoding='utf-8') as file:
        file_content = file.read()
    user_tz = get_user_timezone(file_content)
    new_row = f"| {user} |"
    is_eliminated = False
    absent_count = 0
    current_week = None

    user_current_day = datetime.now(user_tz).replace(
        hour=0, minute=0, second=0, microsecond=0)
    for date in get_date_range():
        # 获取用户时区和当地时间进行比较，如果用户打卡时间大于当地时间，则不显示- timedelta(days=1)
        user_datetime = date.astimezone(pytz.UTC).replace(
            hour=0, minute=0, second=0, microsecond=0)
        if is_eliminated or (user_datetime > user_current_day and user_datetime.day > user_current_day.day):
            new_row += " |"
        else:
            user_date = user_datetime
            # 检查是否是新的一周
            week = user_date.isocalendar()[1]  # 获取ISO日历周数
            if week != current_week:
                current_week = week
                absent_count = 0  # 重置缺勤计数

            status = user_status.get(user_date, "")

            if status == "⭕️":
                absent_count += 1
                if absent_count > MAX_MISS_TIMES:
                    is_eliminated = True
                    new_row += " ❌ |"
                else:
                    new_row += " ⭕️ |"
            else:
                new_row += f" {status} |"

    return new_row + '\n'

def get_all_user_files():
    exclude_prefixes = ('template', 'readme')
    return [f[:-len(FILE_SUFFIX)] for f in os.listdir('.')
            if f.lower().endswith(FILE_SUFFIX.lower()) 
            and not f.lower().startswith(exclude_prefixes)]

def update_readme(content):
    try:
        start_index = content.find(TABLE_START_MARKER)
        end_index = content.find(TABLE_END_MARKER)
        if start_index == -1 or end_index == -1:
            logging.error(
                "Error: Couldn't find the table markers in README.md")
            return content

        new_table = [
            f'{TABLE_START_MARKER}\n',
            f'| {FIELD_NAME} | ' +
            ' | '.join(date.strftime("%m.%d").lstrip('0')
                       for date in get_date_range()) + ' |\n',
            '| ------------- | ' +
            ' | '.join(['----' for _ in get_date_range()]) + ' |\n'
        ]

        existing_users = set()
        table_rows = content[start_index +
                             len(TABLE_START_MARKER):end_index].strip().split('\n')[2:]

        for row in table_rows:
            match = re.match(r'\|\s*([^|]+)\s*\|', row)
            if match:
                display_name = match.group(1).strip()
                if display_name:  # 检查 display_name 是否为非空
                    existing_users.add(display_name)
                    new_table.append(generate_user_row(display_name))
                else:
                    logging.warning(
                        f"Skipping empty display name in row: {row}")
            else:
                logging.warning(f"Skipping invalid row: {row}")

        new_users = set(get_all_user_files()) - existing_users
        for user in new_users:
            if user.strip():  # 确保用户名不是空的或只包含空格
                new_table.append(generate_user_row(user))
                logging.info(f"Added new user: {user}")
            else:
                logging.warning(f"Skipping empty user: '{user}'")
        new_table.append(f'{TABLE_END_MARKER}')
        return content[:start_index] + ''.join(new_table) + content[end_index + len(TABLE_END_MARKER):]
    except Exception as e:
        logging.error(f"Error in update_readme: {str(e)}")
        return content

def main():
    try:
        with open(README_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
        new_content = update_readme(content)
        with open(README_FILE, 'w', encoding='utf-8') as file:
            file.write(new_content)
        logging.info(new_content)
        logging.info("README.md has been successfully updated.")
    except Exception as e:
      logging.error(f"An error occurred in main function: {str(e)}")


if __name__ == "__main__":
    main()
