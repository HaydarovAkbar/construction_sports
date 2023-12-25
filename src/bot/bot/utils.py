from datetime import datetime
import requests


def tg_parse(msg_id, channel):
    try:
        URL = f"https://t.me/{channel}/{msg_id}?embed=1&tme_mode=1"
        site = requests.get(URL)
        txt = site.text
        start_with_count = txt.find('tgme_widget_message_views')
        end_with_count = txt.index('span', start_with_count, start_with_count + 1000)
        start_with_time = txt.find('datetime')
        end_with_time = txt.index('datetime', start_with_time + 20, start_with_time + 100)
        count_v = {'K': 1000, "M": 1000000}
        view_count = txt[start_with_count + 27:end_with_count - 2]
        for key, value in count_v.items():
            if key in view_count:
                view_count = view_count.replace(key, '')
                view_count = float(view_count) * value
                break
        view_count = int(view_count)
        date_ = txt[start_with_time + 10:end_with_time - 9]
        post_date = datetime(year=int(date_[:4]), month=int(date_[5:7]), day=int(date_[8:10]))
        days = (datetime.now() - post_date).days
        if days > 100:
            return False
        return [view_count, date_]
    except Exception:
        return []
