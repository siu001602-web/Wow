import streamlit as st
import pandas as pd
import random
import time

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="버튜버 실시간 노래 차트 게임",
    page_icon="🎵",
    layout="wide"
)

# 2. 멤버별 테마 색상 및 스타일 정의 (추후 멤버 추가 시 여기에만 추가하면 됨)
MEMBER_THEMES = {
    "유니": {
        "color": "#9B72CF",      # 보라색 계열 (아야츠노 유니 시그니처 컬러)
        "bg_color": "#F5EEFF",   # 연한 보라색 배경
        "badge": "🦄 유니"
    },
    # 예시: 나중에 다른 멤버 추가할 때 아래 주석을 풀고 사용하세요!
    # "칸나": {
    #     "color": "#4A90E2",
    #     "bg_color": "#EBF3FA",
    #     "badge": "🐉 칸나"
    # },
    # "시로": {
    #     "color": "#7F8C8D",
    #     "bg_color": "#F2F4F4",
    #     "badge": "🐺 시로"
    # }
}

# 3. 초기 노래 데이터 (단위: 회)
INITIAL_SONGS = [
    {"멤버": "유니", "곡명": "긍지높은 아이돌", "조회수": 1190000},
    {"멤버": "유니", "곡명": "베텔기우스", "조회수": 1720000},
    {"멤버": "유니", "곡명": "사랑의 말IV", "조회수": 730000},
    {"멤버": "유니", "곡명": "굿바이 선언", "조회수": 2100000},
    {"멤버": "유니", "곡명": "아이돌", "조회수": 780000},
    {"멤버": "유니", "곡명": "내꺼 하는 법", "조회수": 7120000},
    {"멤버": "유니", "곡명": "Mela!", "조회수": 1140000},
    {"멤버": "유니", "곡명": "두근어질", "조회수": 720000},
    {"멤버": "유니", "곡명": "SUPERPOWER", "조회수": 240000},
    {"멤버": "유니", "곡명": "점묘의 노래(with 칸나)", "조회수": 3130000},
    {"멤버": "유니", "곡명": "해피 신디사이저(with 시로)", "조회수": 1110000},
    {"멤버": "유니", "곡명": "연애 서큘레이션", "조회수": 850000},
    {"멤버": "유니", "곡명": "SUPADOPA", "조회수": 6200000},
    {"멤버": "유니", "곡명": "라일락", "조회수": 1380000},
    {"멤버": "유니", "곡명": "삐질게", "조회수": 1190000},
    {"멤버": "유니", "곡명": "참생활", "조회수": 400000},
    {"멤버": "유니", "곡명": "오네가이 달링", "조회수": 500000},
]

# 4. 세션 상태(게임 데이터) 초기화
if "songs" not in st.session_state:
    st.session_state.songs = [dict(song, 변동=0, 이전순위=i+1) for i, song in enumerate(INITIAL_SONGS)]
    st.session_state.tick = 0
    st.session_state.is_running = True

# 조회수 포맷팅 함수 (예: 1195400 -> 119.54만 (1,195,400))
def format_views(views):
    man = views / 10000
    return f"{man:,.2f}만 ({views:,}회)"

# 상단 타이틀 및 컨트롤 버튼
st.title("🎵 실시간 노래 차트 시뮬레이터")

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    if st.button("⏯️ 일시정지 / 재개", use_container_width=True):
        st.session_state.is_running = not st.session_state.is_running
with col2:
    if st.button("🔄 차트 초기화", use_container_width=True):
        st.session_state.songs = [dict(song, 변동=0, 이전순위=i+1) for i, song in enumerate(INITIAL_SONGS)]
        st.session_state.tick = 0
        st.rerun()

# 5. 10초마다 자동 실행되는 실시간 차트 영역
@st.fragment(run_every=10)
def live_chart():
    # 실행 중일 때만 조회수 증가 로직 작동 (첫 로딩인 tick == 0 제외)
    if st.session_state.is_running and st.session_state.tick > 0:
        # 이전 순위 기록
        sorted_prev = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
        prev_ranks = {song["곡명"]: idx + 1 for idx, song in enumerate(sorted_prev)}

        # 각 곡마다 100 ~ 10,000 조회수 랜덤 증가
        for song in st.session_state.songs:
            inc = random.randint(100, 10000)
            song["조회수"] += inc
            song["변동"] = inc
            song["이전순위"] = prev_ranks[song["곡명"]]

    st.session_state.tick += 1

    # 조회수 내림차순 정렬
    current_sorted = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)

    status_text = "🟢 실시간 집계 중 (10초마다 갱신)" if st.session_state.is_running else "⏸️ 일시정지됨"
    st.caption(f"{status_text} | 경과 시간: {(st.session_state.tick - 1) * 10}초")

    # HTML/CSS 커스텀 차트 렌더링 (멤버별 고유 색상과 배지 적용)
    for idx, song in enumerate(current_sorted):
        rank = idx + 1
        member = song["멤버"]
        theme = MEMBER_THEMES.get(member, {"color": "#888888", "bg_color": "#F0F0F0", "badge": member})

        # 순위 변동 계산
        if st.session_state.tick == 1:
            rank_diff_html = '<span style="color: gray; font-size: 0.85em;">-</span>'
        else:
            diff = song["이전순위"] - rank
            if diff > 0:
                rank_diff_html = f'<span style="color: #E74C3C; font-weight: bold; font-size: 0.85em;">▲ {diff}</span>'
            elif diff < 0:
                rank_diff_html = f'<span style="color: #3498DB; font-weight: bold; font-size: 0.85em;">▼ {abs(diff)}</span>'
            else:
                rank_diff_html = '<span style="color: gray; font-size: 0.85em;">-</span>'

        # 증가량 표시
        inc_text = f"+{song['변동']:,}" if song["변동"] > 0 else "시작 조회수"

        # 카드 형태의 차트 행 출력
        st.markdown(
            f"""
            <div style="
                display: flex;
                align-items: center;
                justify-content: space-between;
                background-color: {theme['bg_color']};
                border-left: 8px solid {theme['color']};
                padding: 12px 20px;
                margin-bottom: 8px;
                border-radius: 8px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.08);
            ">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 1.3em; font-weight: 800; width: 35px; text-align: center; color: #222;">
                        {rank}
                    </div>
                    <div style="width: 45px; text-align: center;">
                        {rank_diff_html}
                    </div>
                    <span style="
                        background-color: {theme['color']};
                        color: white;
                        padding: 4px 10px;
                        border-radius: 15px;
                        font-size: 0.85em;
                        font-weight: bold;
                    ">
                        {theme['badge']}
                    </span>
                    <span style="font-size: 1.1em; font-weight: 700; color: #111;">
                        {song['곡명']}
                    </span>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 1.05em; font-weight: 700; color: #222;">
                        {format_views(song['조회수'])}
                    </div>
                    <div style="font-size: 0.8em; color: #E67E22; font-weight: 600;">
                        {inc_text}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

live_chart()
