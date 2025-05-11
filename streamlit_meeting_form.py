import streamlit as st
import datetime
import pytz

kst = pytz.timezone("Asia/Seoul")
now_kst = datetime.datetime.now(kst)
today_kst = now_kst.date()
time_kst = now_kst.strftime("%H:%M")

room = {
    "company": "한국금기",
    "admin": "김강윤",
    "team": "건설팀(16층)",
    "info": {
        "date": str(today_kst),
        "time": time_kst,
        "place": "현장 A",
        "task": "고소작업"
    },
    "attendees": ["김강윤"],
    "discussion": [("1", "1"), ("1", "1")],
    "additional": "1",
    "tasks": [("1", "1", str(today_kst))],
    "confirmations": ["김강윤"]
}

st.set_page_config(layout="wide")
st.title("🖨 인쇄용 회의 미리보기 테스트")

html = f'''
<div style="font-family: 'NanumGothic', sans-serif; font-size:14px; padding:30px; line-height:1.8;">
    <h2 style="text-align:center; font-size:20pt; margin-bottom:4px;">
        📋 Toolbox Talk 회의록 - [{room["team"]}]
    </h2>
    <p style="text-align:center; font-size:12pt; margin-top:0;">회사명: {room["company"]}</p>
    <p><b>📅 날짜:</b> {room["info"]["date"]} &nbsp;&nbsp; <b>🕒 시간:</b> {room["info"]["time"]}</p>
    <p><b>📍 장소:</b> {room["info"]["place"]} &nbsp;&nbsp; <b>🛠 작업:</b> {room["info"]["task"]}</p>
    <p><b>👤 리더:</b> {room["admin"]}</p>

    <h3 style="margin-top:30px;">👥 참석자</h3>
    <ul>{''.join([f"<li>{name}</li>" for name in room["attendees"]])}</ul>

    <h3 style="margin-top:30px;">🧠 논의 내용</h3>
    <ol>{''.join([f"<li><b>{r}</b> → {m}</li>" for r, m in room["discussion"]])}</ol>

    <h3 style="margin-top:30px;">➕ 추가 논의</h3>
    <p>{room["additional"]}</p>

    <h3 style="margin-top:30px;">✅ 결정사항 및 조치</h3>
    <ul>{''.join([f"<li>{p}: {r} (예정일: {d})</li>" for p, r, d in room["tasks"]])}</ul>

    <h3 style="margin-top:30px;">✍ 확인자</h3>
    <ul>{''.join([f"<li>{n} (확인 완료)</li>" for n in room["confirmations"]])}</ul>

    <hr style="margin-top:40px;">
    <p style="text-align:right; font-size:10pt;">App. support by HealSE Co., Ltd.</p>
</div>
'''

# height 충분히 크게 설정
st.components.v1.html(html, height=3000, scrolling=True)