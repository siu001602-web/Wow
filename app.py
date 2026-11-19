import streamlit as st
import pandas as pd
import random

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="버튜버 실시간 노래 차트 게임",
    page_icon="🎵",
    layout="wide"
)

# 2. 멤버별 테마 색상 및 스타일 정의
MEMBER_THEMES = {
    "유니": {
        "color": "#9B72CF",      # 보라색 계열
        "bg_color": "#F5EEFF",   # 연한 보라색 배경
        "badge": "🦄 유니"
    },
    "후야": {
        "color": "#FF6B8B",      # 코랄 핑크 계열
        "bg_color": "#FFF0F4",   # 연한 핑크색 배경
        "badge": "🐉 후야"
    },
    "마시로": {
        "color": "#607D8B",      # 슬레이트 실버/블루 계열
        "bg_color": "#ECEFF1",   # 연한 그레이 화이트 배경
        "badge": "🐱 마시로"
    },
    "타비": {
        "color": "#2980B9",      # 네이비/블루 계열
        "bg_color": "#EAF2F8",   # 연한 블루 배경
        "badge": "🧭 타비"
    },
    "히나": {
        "color": "#FF8DA1",      # 핑크 계열
        "bg_color": "#FFF0F3",
        "badge": "🏫 히나"
    },
    "시로": {
        "color": "#7F8C8D",      # 그레이 계열
        "bg_color": "#F2F4F4",
        "badge": "🐱 시로"
    },
}

# 3. 초기 노래 데이터 (단위: 회 / original=True는 오리지널 곡)
INITIAL_SONGS = [
    # 유니
    {"멤버": "유니", "곡명": "긍지높은 아이돌", "조회수": 1190000, "original": False},
    {"멤버": "유니", "곡명": "베텔기우스", "조회수": 1720000, "original": False},
    {"멤버": "유니", "곡명": "사랑의 말IV", "조회수": 730000, "original": False},
    {"멤버": "유니", "곡명": "굿바이 선언", "조회수": 2100000, "original": False},
    {"멤버": "유니", "곡명": "아이돌", "조회수": 780000, "original": False},
    {"멤버": "유니", "곡명": "내꺼 하는 법", "조회수": 7120000, "original": True},
    {"멤버": "유니", "곡명": "Mela!", "조회수": 1140000, "original": False},
    {"멤버": "유니", "곡명": "두근어질", "조회수": 720000, "original": False},
    {"멤버": "유니", "곡명": "SUPERPOWER", "조회수": 240000, "original": False},
    {"멤버": "유니", "곡명": "점묘의 노래(with 칸나)", "조회수": 3130000, "original": False},
    {"멤버": "유니", "곡명": "해피 신디사이저(with 시로)", "조회수": 1110000, "original": False},
    {"멤버": "유니", "곡명": "연애 서큘레이션", "조회수": 850000, "original": False},
    {"멤버": "유니", "곡명": "SUPADOPA", "조회수": 6200000, "original": True},
    {"멤버": "유니", "곡명": "라일락", "조회수": 1380000, "original": False},
    {"멤버": "유니", "곡명": "삐질게", "조회수": 1190000, "original": True},
    {"멤버": "유니", "곡명": "참생활", "조회수": 400000, "original": False},
    {"멤버": "유니", "곡명": "오네가이 달링", "조회수": 500000, "original": False},
    
    # 후야
    {"멤버": "후야", "곡명": "오츠카레summer(with 나나)", "조회수": 850000, "original": False},
    {"멤버": "후야", "곡명": "푸른 산호초", "조회수": 640000, "original": False},
    {"멤버": "후야", "곡명": "BOOO!", "조회수": 440000, "original": False},
    {"멤버": "후야", "곡명": "Melt!", "조회수": 480000, "original": False},
    {"멤버": "후야", "곡명": "푸른 하늘의 랩소디", "조회수": 970000, "original": False},
    {"멤버": "후야", "곡명": "CHEWING LUV", "조회수": 380000, "original": False},
    {"멤버": "후야", "곡명": "팝핀 캔디☆피버(with 유니)", "조회수": 1740000, "original": False},
    {"멤버": "후야", "곡명": "별자리가 될 수 있다면", "조회수": 1570000, "original": False},

    # 마시로
    {"멤버": "마시로", "곡명": "봄꿈", "조회수": 1680000, "original": True},
    {"멤버": "마시로", "곡명": "Dear my fairy", "조회수": 420000, "original": True},
    {"멤버": "마시로", "곡명": "Pale", "조회수": 2400000, "original": False},
    {"멤버": "마시로", "곡명": "퀘스천", "조회수": 2250000, "original": False},
    {"멤버": "마시로", "곡명": "구르는 바위, 네게 아침이 내린다", "조회수": 170000, "original": False},
    {"멤버": "마시로", "곡명": "메이드지상주의(with 린)", "조회수": 340000, "original": False},
    {"멤버": "마시로", "곡명": "쿵쿵 앞으로", "조회수": 340000, "original": False},
    {"멤버": "마시로", "곡명": "그나라의 왕가는 이상해(with 리제)", "조회수": 420000, "original": False},
    {"멤버": "마시로", "곡명": "병명 상사병", "조회수": 550000, "original": False},
    {"멤버": "마시로", "곡명": "슈가로스", "조회수": 720000, "original": False},
    {"멤버": "마시로", "곡명": "우주 비행사의 노래", "조회수": 750000, "original": False},
    {"멤버": "마시로", "곡명": "댄스 로봇 댄스", "조회수": 770000, "original": False},
    {"멤버": "마시로", "곡명": "츄 다양성", "조회수": 1030000, "original": False},
    {"멤버": "마시로", "곡명": "연예인", "조회수": 1100000, "original": False},
    {"멤버": "마시로", "곡명": "네 기꺼이(with 부키)", "조회수": 1180000, "original": False},
    {"멤버": "마시로", "곡명": "안녕, 꽃도둑씨", "조회수": 1390000, "original": False},
    {"멤버": "마시로", "곡명": "사랑하고 있는거야(with 타비)", "조회수": 1500000, "original": False},

    # 타비
    {"멤버": "타비", "곡명": "여로", "조회수": 1580000, "original": True},
    {"멤버": "타비", "곡명": "그 여름의 어느날", "조회수": 1830000, "original": False},
    {"멤버": "타비", "곡명": "그 여름에 피어나", "조회수": 1270000, "original": False},
    {"멤버": "타비", "곡명": "낮에 뜨는 달", "조회수": 4230000, "original": False},
    {"멤버": "타비", "곡명": "첫사랑", "조회수": 3160000, "original": False},
    {"멤버": "타비", "곡명": "HERO", "조회수": 2220000, "original": False},
    {"멤버": "타비", "곡명": "BE SOMEBODY", "조회수": 1720000, "original": False},
    {"멤버": "타비", "곡명": "사신", "조회수": 2980000, "original": False},
    {"멤버": "타비", "곡명": "안녕, 또 언젠가!(with 시로)", "조회수": 600000, "original": False},
    {"멤버": "타비", "곡명": "새봄의 노래", "조회수": 770000, "original": False},
    {"멤버": "타비", "곡명": "야화(with 나나)", "조회수": 1910000, "original": False},
    {"멤버": "타비", "곡명": "Ref:rain", "조회수": 1300000, "original": False},
    {"멤버": "타비", "곡명": "Healer", "조회수": 1070000, "original": False},
    {"멤버": "타비", "곡명": "Soda pop", "조회수": 910000, "original": False},
    {"멤버": "타비", "곡명": "Number one rockstar", "조회수": 530000, "original": False},
    {"멤버": "타비", "곡명": "한페이지가 될 수 있게", "조회수": 1080000, "original": False},
    {"멤버": "타비", "곡명": "사랑 감기에 실려", "조회수": 1140000, "original": False},
    {"멤버": "타비", "곡명": "밤새도록 널 생각해", "조회수": 730000, "original": False},
    {"멤버": "타비", "곡명": "행운을 빌어줘", "조회수": 1350000, "original": False},
    {"멤버": "타비", "곡명": "High Hopes", "조회수": 1250000, "original": False},
    {"멤버": "타비", "곡명": "물떼새", "조회수": 940000, "original": False},
]

# 4. 세션 상태(게임 데이터) 초기화
def init_songs():
    sorted_init = sorted(INITIAL_SONGS, key=lambda x: x["조회수"], reverse=True)
    return [dict(song, 변동=0, prev_rank_1m=i+1, is_trending=False) for i, song in enumerate(sorted_init)]

if "songs" not in st.session_state:
    st.session_state.songs = init_songs()
    st.session_state.tick = 0
    st.session_state.is_running = True
    st.session_state.recent_trending = [] # 이번 턴에 인급동이 뜬 곡 정보 저장용
else:
    for i, song in enumerate(st.session_state.songs):
        if "prev_rank_1m" not in song:
            song["prev_rank_1m"] = i + 1
        if "변동" not in song:
            song["변동"] = 0
        if "original" not in song:
            song["original"] = False
        if "is_trending" not in song:
            song["is_trending"] = False

if "recent_trending" not in st.session_state:
    st.session_state.recent_trending = []

# 조회수 포맷팅 함수
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
        st.session_state.songs = init_songs()
        st.session_state.tick = 0
        st.session_state.recent_trending = []
        st.rerun()

# 5. 3초마다 자동 실행되는 실시간 차트 영역
@st.fragment(run_every=3)
def live_chart():
    triggered_list = []
    
    if st.session_state.is_running and st.session_state.tick > 0:
        # 매 20틱(3초 * 20 = 60초 = 1분)마다 현재 순위를 '1분 전 순위'로 갱신
        if st.session_state.tick % 20 == 0:
            current_sorted_for_snapshot = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
            snapshot_ranks = {(song["멤버"], song["곡명"]): idx + 1 for idx, song in enumerate(current_sorted_for_snapshot)}
            for song in st.session_state.songs:
                song["prev_rank_1m"] = snapshot_ranks[(song["멤버"], song["곡명"])]

        # 각 곡마다 0.1% 확률(0.001)로 인급동(Trending) 발동 체크
        for song in st.session_state.songs:
            if random.random() < 0.001:
                song["is_trending"] = True
                inc = random.randint(1000, 50000)
                triggered_list.append((song["곡명"], inc))
            else:
                song["is_trending"] = False
                inc = random.randint(100, 10000)
            
            song["조회수"] += inc
            song["변동"] = inc

    st.session_state.tick += 1
    st.session_state.recent_trending = triggered_list

    # 인급동 발동 알림 배너 표시 영역
    if st.session_state.recent_trending:
        for song_name, inc_val in st.session_state.recent_trending:
            st.markdown(
                f"""
                <div style="
                    background-color: #FFF3CD;
                    border: 2px solid #FFEEBA;
                    color: #856404;
                    padding: 10px 15px;
                    border-radius: 8px;
                    margin-bottom: 10px;
                    font-weight: bold;
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    animation: fadeIn 0.5s;
                ">
                    🔥 <span><b>[{song_name}]</b>이(가) 인급동의 여파로 <b>+{inc_val:,}회</b> 증가했습니다!</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # 조회수 내림차순 정렬
    current_sorted = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)

    status_text = "🟢 실시간 집계 중 (3초 갱신 / 1분 단위 순위 반영)" if st.session_state.is_running else "⏸️ 일시정지됨"
    st.caption(f"{status_text} | 총 {len(current_sorted)}곡 경쟁 중 | 경과 시간: {(st.session_state.tick - 1) * 3}초")

    # HTML/CSS 커스텀 차트 렌더링
    for idx, song in enumerate(current_sorted):
        rank = idx + 1
        member = song["멤버"]
        
        # 특수 듀엣 배지 처리
        if song["곡명"] == "Dear my fairy":
            badge_html = '<span style="background: linear-gradient(135deg, #FF8DA1, #607D8B); color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.85em; font-weight: bold;">🏫히나 & 🐱마시로</span>'
            left_border_color = "#FF8DA1"
            bg_color = "#FFF5F7"
        else:
            theme = MEMBER_THEMES.get(member, {"color": "#888888", "bg_color": "#F0F0F0", "badge": member})
            badge_html = f'<span style="background-color: {theme["color"]}; color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.85em; font-weight: bold;">{theme["badge"]}</span>'
            left_border_color = theme["color"]
            bg_color = theme["bg_color"]

        # 오리지널 곡 태그
        original_tag = ' <span style="background-color: #FFD700; color: #333; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">✨ 오리지널</span>' if song.get("original", False) else ''

        # 인급동 발동 태그
        trending_tag = ' <span style="background-color: #FF4757; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">🔥 [인급동]</span>' if song.get("is_trending", False) else ''

        # 1분 전 순위와 현재 순위 비교
        if st.session_state.tick < 20:
            rank_diff_html = '<span style="color: gray; font-size: 0.85em;">-</span>'
        else:
            prev_rank = song.get("prev_rank_1m", rank)
            diff = prev_rank - rank
            if diff > 0:
                rank_diff_html = f'<span style="color: #E74C3C; font-weight: bold; font-size: 0.85em;">▲ {diff}</span>'
            elif diff < 0:
                rank_diff_html = f'<span style="color: #3498DB; font-weight: bold; font-size: 0.85em;">▼ {abs(diff)}</span>'
            else:
                rank_diff_html = '<span style="color: gray; font-size: 0.85em;">-</span>'

        inc_text = f"+{song['변동']:,}" if st.session_state.tick > 1 else "시작 조회수"

        st.markdown(
            f"""
            <div style="
                display: flex;
                align-items: center;
                justify-content: space-between;
                background-color: {bg_color};
                border-left: 8px solid {left_border_color};
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
                    {badge_html}
                    <span style="font-size: 1.1em; font-weight: 700; color: #111;">
                        {song['곡명']}{original_tag}{trending_tag}
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
