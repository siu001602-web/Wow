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
        "bg_color": "#FFF0F3",   # 연한 핑크 배경
        "badge": "🏫 히나"
    },
    "리제": {
        "color": "#C0392B",      # 진한 빨강 계열
        "bg_color": "#FDEDEC",   # 연한 빨강 배경
        "badge": "🧛‍♀️ 리제"
    },
    "부키": {
        "color": "#F1C40F",      # 노란색 계열
        "bg_color": "#FEF9E7",   # 연한 노란색 배경
        "badge": "🦊 부키"
    },
    "나나": {
        "color": "#27AE60",      # 연두색 계열
        "bg_color": "#EAFAF1",   # 연한 연두색 배경
        "badge": "🔫 나나"
    },
    "린": {
        "color": "#BDC3C7",      # 흰색/실버 계열
        "bg_color": "#F8F9F9",   # 연한 흰/회색 배경
        "badge": "👗 린"
    },
    "유니버스": {
        "color": "#16A085",      # 청록색 계열
        "bg_color": "#E8F8F5",   # 연한 청록 배경
        "badge": "✨ 유니버스"
    },
    "시로": {
        "color": "#7F8C8D",      # 그레이 계열
        "bg_color": "#F2F4F4",   # 연한 그레이 배경
        "badge": "🐱 시로"
    },
}

# 3. 초기 노래 데이터 (단위: 회 / original=True는 오리지널 곡)
INITIAL_SONGS = [
    # 유니버스 (단체곡)
    {"멤버": "유니버스", "곡명": "Stars Align", "조회수": 1410000, "original": True},
    {"멤버": "유니버스", "곡명": "마음악보", "조회수": 990000, "original": True},

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

    # 히나
    {"멤버": "히나", "곡명": "하나", "조회수": 1130000, "original": True},
    {"멤버": "히나", "곡명": "솔라리스", "조회수": 230000, "original": True},
    {"멤버": "히나", "곡명": "불꽃", "조회수": 240000, "original": True},
    {"멤버": "히나", "곡명": "꿈의 신호", "조회수": 360000, "original": True},
    {"멤버": "히나", "곡명": "투니버스 메들리", "조회수": 1030000, "original": False},
    {"멤버": "히나", "곡명": "낙향", "조회수": 8310000, "original": False},
    {"멤버": "히나", "곡명": "드라마", "조회수": 1630000, "original": False},
    {"멤버": "히나", "곡명": "그저 네게 맑아라", "조회수": 3640000, "original": False},
    {"멤버": "히나", "곡명": "라푼젤", "조회수": 1960000, "original": False},
    {"멤버": "히나", "곡명": "Sweet Dreams, My dear", "조회수": 2930000, "original": False},
    {"멤버": "히나", "곡명": "봄을 기다리다", "조회수": 2120000, "original": False},
    {"멤버": "히나", "곡명": "새벽과 반딧불이", "조회수": 2140000, "original": False},
    {"멤버": "히나", "곡명": "하루카", "조회수": 1120000, "original": False},
    {"멤버": "히나", "곡명": "17살의 노래", "조회수": 2640000, "original": False},
    {"멤버": "히나", "곡명": "피날레", "조회수": 5090000, "original": False},
    {"멤버": "히나", "곡명": "I really want to stay at your house", "조회수": 5360000, "original": False},
    {"멤버": "히나", "곡명": "JANE DOE(with 린)", "조회수": 2070000, "original": False},
    {"멤버": "히나", "곡명": "ray(with 리제)", "조회수": 1570000, "original": False},
    {"멤버": "히나", "곡명": "Alice in musicland", "조회수": 2300000, "original": False},
    {"멤버": "히나", "곡명": "Lonely universe", "조회수": 1080000, "original": False},
    {"멤버": "히나", "곡명": "만찬가", "조회수": 3080000, "original": False},
    {"멤버": "히나", "곡명": "Orange", "조회수": 2020000, "original": False},
    {"멤버": "히나", "곡명": "summertime(with 나나)", "조회수": 1930000, "original": False},
    {"멤버": "히나", "곡명": "Lady", "조회수": 1980000, "original": False},
    {"멤버": "히나", "곡명": "악마의 아이", "조회수": 1790000, "original": False},
    {"멤버": "히나", "곡명": "군청", "조회수": 1060000, "original": False},
    {"멤버": "히나", "곡명": "사랑해줘 사랑해줘 사랑해줘", "조회수": 1180000, "original": False},
    {"멤버": "히나", "곡명": "깜빡임", "조회수": 1480000, "original": False},
    {"멤버": "히나", "곡명": "개화", "조회수": 400000, "original": False},
    {"멤버": "히나", "곡명": "크리스마스 송", "조회수": 610000, "original": False},
    {"멤버": "히나", "곡명": "Melt", "조회수": 1240000, "original": False},
    {"멤버": "히나", "곡명": "계절범죄", "조회수": 1590000, "original": False},
    {"멤버": "히나", "곡명": "바다의 유령", "조회수": 1030000, "original": False},
    {"멤버": "히나", "곡명": "Acacia", "조회수": 860000, "original": False},
    {"멤버": "히나", "곡명": "춘수", "조회수": 620000, "original": False},
    {"멤버": "히나", "곡명": "내일 또 보자", "조회수": 680000, "original": False},
    {"멤버": "히나", "곡명": "아틀란티스 소녀", "조회수": 450000, "original": False},
    {"멤버": "히나", "곡명": "타상연화", "조회수": 610000, "original": False},

    # 리제
    {"멤버": "리제", "곡명": "월드 오브 탱크", "조회수": 820000, "original": True},
    {"멤버": "리제", "곡명": "Festa!", "조회수": 1600000, "original": True},
    {"멤버": "리제", "곡명": "괴물", "조회수": 7900000, "original": False},
    {"멤버": "리제", "곡명": "나라는 것", "조회수": 3650000, "original": False},
    {"멤버": "리제", "곡명": "stranger", "조회수": 2070000, "original": False},
    {"멤버": "리제", "곡명": "tayori", "조회수": 1340000, "original": False},
    {"멤버": "리제", "곡명": "절정찬가", "조회수": 3240000, "original": False},
    {"멤버": "리제", "곡명": "선잠", "조회수": 6600000, "original": False},
    {"멤버": "리제", "곡명": "괴수의 꽃노래", "조회수": 4330000, "original": False},
    {"멤버": "리제", "곡명": "Melt", "조회수": 4470000, "original": False},
    {"멤버": "리제", "곡명": "프라이드 혁명", "조회수": 2410000, "original": False},
    {"멤버": "리제", "곡명": "Drowning", "조회수": 12520000, "original": False},
    {"멤버": "리제", "곡명": "Hit on shot", "조회수": 2740000, "original": True},
    {"멤버": "리제", "곡명": "밀월", "조회수": 1070000, "original": False},
    {"멤버": "리제", "곡명": "Viva La Vida", "조회수": 2470000, "original": False},
    {"멤버": "리제", "곡명": "끝나지 않은 노래", "조회수": 750000, "original": False},
    {"멤버": "리제", "곡명": "제이팝 매쉬업!", "조회수": 2290000, "original": False},
    {"멤버": "리제", "곡명": "APT(with 린)", "조회수": 2450000, "original": False},
    {"멤버": "리제", "곡명": "내일의 밤하늘 초계반", "조회수": 11540000, "original": False},
    {"멤버": "리제", "곡명": "벛꽃,너,그리고 나", "조회수": 2920000, "original": False},
    {"멤버": "리제", "곡명": "뱀파이어", "조회수": 3160000, "original": False},
    {"멤버": "리제", "곡명": "취한 줄을 모르고", "조회수": 2620000, "original": False},
    {"멤버": "리제", "곡명": "Golden(with 린, 나나)", "조회수": 4040000, "original": False},
    {"멤버": "리제", "곡명": "SHANTI", "조회수": 1120000, "original": False},
    {"멤버": "리제", "곡명": "Surges", "조회수": 5360000, "original": False},
    {"멤버": "리제", "곡명": "프로포즈", "조회수": 2240000, "original": False},
    {"멤버": "리제", "곡명": "바니걸", "조회수": 2610000, "original": False},
    {"멤버": "리제", "곡명": "가면무도회", "조회수": 520000, "original": False},
    {"멤버": "리제", "곡명": "JANE DOE", "조회수": 1440000, "original": False},
    {"멤버": "리제", "곡명": "star walkin'", "조회수": 1010000, "original": False},
    {"멤버": "리제", "곡명": "출항", "조회수": 17180000, "original": False},
    {"멤버": "리제", "곡명": "케세라세라", "조회수": 3010000, "original": False},
    {"멤버": "리제", "곡명": "주름 맞추기", "조회수": 850000, "original": False},
    {"멤버": "리제", "곡명": "Stellar stellar", "조회수": 1110000, "original": False},
    {"멤버": "리제", "곡명": "orion", "조회수": 1160000, "original": False},
    {"멤버": "리제", "곡명": "Hollowness", "조회수": 990000, "original": False},
    {"멤버": "리제", "곡명": "무대에 서서", "조회수": 670000, "original": False},
    {"멤버": "리제", "곡명": "청록", "조회수": 1950000, "original": False},
    {"멤버": "리제", "곡명": "미랫빛 라이더", "조회수": 780000, "original": False},
    {"멤버": "리제", "곡명": "심월과 달의 노래", "조회수": 590000, "original": False},
    {"멤버": "리제", "곡명": "로스트원의 호곡", "조회수": 1900000, "original": False},

    # 부키
    {"멤버": "부키", "곡명": "베리베리스트로베리", "조회수": 1370000, "original": True},
    {"멤버": "부키", "곡명": "너에게 메롱", "조회수": 7870000, "original": False},
    {"멤버": "부키", "곡명": "여우비", "조회수": 5110000, "original": False},
    {"멤버": "부키", "곡명": "Leo", "조회수": 3440000, "original": False},
    {"멤버": "부키", "곡명": "Sabotage", "조회수": 1540000, "original": False},
    {"멤버": "부키", "곡명": "겨울의 선물", "조회수": 1280000, "original": False},
    {"멤버": "부키", "곡명": "Sos", "조회수": 890000, "original": False},
    {"멤버": "부키", "곡명": "있잖아 있잖아 있잖아(with 리코)", "조회수": 1740000, "original": False},
    {"멤버": "부키", "곡명": "눈싸움", "조회수": 2010000, "original": False},
    {"멤버": "부키", "곡명": "UNDEAD", "조회수": 2450000, "original": False},
    {"멤버": "부키", "곡명": "푸름과 여름", "조회수": 2410000, "original": False},
    {"멤버": "부키", "곡명": "KING(with 린)", "조회수": 1730000, "original": False},
    {"멤버": "부키", "곡명": "생명에게 미움받고 있어", "조회수": 3520000, "original": False},
    {"멤버": "부키", "곡명": "메리크리", "조회수": 840000, "original": False},
    {"멤버": "부키", "곡명": "Daybreak frontline", "조회수": 2050000, "original": False},
    {"멤버": "부키", "곡명": "러브레터", "조회수": 1090000, "original": False},
    {"멤버": "부키", "곡명": "행복에 대해 내가 생각한것", "조회수": 1630000, "original": False},
    {"멤버": "부키", "곡명": "나에게 꽃다발", "조회수": 530000, "original": False},
    {"멤버": "부키", "곡명": "친애하는 소년이여", "조회수": 1660000, "original": False},
    {"멤버": "부키", "곡명": "mosi mosi?", "조회수": 590000, "original": False},
    {"멤버": "부키", "곡명": "혁명도중", "조회수": 900000, "original": False},
    {"멤버": "부키", "곡명": "호시아이[4k]", "조회수": 240000, "original": False},
    {"멤버": "부키", "곡명": "StaRt[4k]", "조회수": 240000, "original": False},
    {"멤버": "부키", "곡명": "신의 뜻대로[4k] (with 린,리코,나나)", "조회수": 1380000, "original": False},
    {"멤버": "부키", "곡명": "잡어[4k] (with 시로)", "조회수": 170000, "original": False},
    {"멤버": "부키", "곡명": "숨바꼭질[4k]", "조회수": 330000, "original": False},

    # 나나
    {"멤버": "나나", "곡명": "Hush trap", "조회수": 1150000, "original": True},
    {"멤버": "나나", "곡명": "Born to run", "조회수": 1930000, "original": True},
    {"멤버": "나나", "곡명": "가짜 얼굴", "조회수": 3690000, "original": False},
    {"멤버": "나나", "곡명": "푸른 산호초", "조회수": 1450000, "original": False},
    {"멤버": "나나", "곡명": "Some like it hot", "조회수": 4600000, "original": False},
    {"멤버": "나나", "곡명": "신 같네", "조회수": 2670000, "original": False},
    {"멤버": "나나", "곡명": "비행정", "조회수": 6250000, "original": False},
    {"멤버": "나나", "곡명": "실•부•프레지던트", "조회수": 1330000, "original": False},
    {"멤버": "나나", "곡명": "Beyond the way(with 리코,린)", "조회수": 2680000, "original": False},
    {"멤버": "나나", "곡명": "역몽(with 린)", "조회수": 2860000, "original": False},
    {"멤버": "나나", "곡명": "모니터링", "조회수": 2030000, "original": False},
    {"멤버": "나나", "곡명": "Grand Escape(with 린,부키,리코)", "조회수": 1900000, "original": False},
    {"멤버": "나나", "곡명": "Enemy", "조회수": 4690000, "original": False},
    {"멤버": "나나", "곡명": "summertime", "조회수": 580000, "original": False},
    {"멤버": "나나", "곡명": "걘 아니야", "조회수": 3080000, "original": False},
    {"멤버": "나나", "곡명": "죽는게 나아", "조회수": 1340000, "original": False},
    {"멤버": "나나", "곡명": "Summer", "조회수": 2400000, "original": False},
    {"멤버": "나나", "곡명": "울려퍼져라(with 부키)", "조회수": 1170000, "original": False},
    {"멤버": "나나", "곡명": "JANE DOE", "조회수": 600000, "original": False},
    {"멤버": "나나", "곡명": "수평선", "조회수": 2430000, "original": False},
    {"멤버": "나나", "곡명": "TOMBOY", "조회수": 1410000, "original": False},
    {"멤버": "나나", "곡명": "JOKER(with 히나)", "조회수": 1220000, "original": False},
    {"멤버": "나나", "곡명": "Rain", "조회수": 2230000, "original": False},
    {"멤버": "나나", "곡명": "Yin and Yang", "조회수": 640000, "original": False},
    {"멤버": "나나", "곡명": "죄와 벌", "조회수": 730000, "original": False},
    {"멤버": "나나", "곡명": "One last kiss", "조회수": 850000, "original": False},
    {"멤버": "나나", "곡명": "Deja vu", "조회수": 500000, "original": False},
    {"멤버": "나나", "곡명": "drivers license", "조회수": 530000, "original": False},
    {"멤버": "나나", "곡명": "Loveit?", "조회수": 910000, "original": False},
    {"멤버": "나나", "곡명": "희극", "조회수": 780000, "original": False},
    {"멤버": "나나", "곡명": "논브레스 오블리주", "조회수": 1150000, "original": False},
    {"멤버": "나나", "곡명": "브레인 롯", "조회수": 980000, "original": False},
    {"멤버": "나나", "곡명": "발랄라이카", "조회수": 610000, "original": False},

    # 린
    {"멤버": "린", "곡명": "Maid My Way", "조회수": 2590000, "original": True},
    {"멤버": "린", "곡명": "불꽃(with 나나)", "조회수": 560000, "original": True},
    {"멤버": "린", "곡명": "유령도쿄", "조회수": 5510000, "original": False},
    {"멤버": "린", "곡명": "안녕, 또 언젠가", "조회수": 3820000, "original": False},
    {"멤버": "린", "곡명": "Rumor", "조회수": 2990000, "original": False},
    {"멤버": "린", "곡명": "무희", "조회수": 4680000, "original": False},
    {"멤버": "린", "곡명": "사랑 감기에 실려", "조회수": 3200000, "original": False},
    {"멤버": "린", "곡명": "Overdose", "조회수": 3520000, "original": False},
    {"멤버": "린", "곡명": "back number", "조회수": 3350000, "original": False},
    {"멤버": "린", "곡명": "Specialz", "조회수": 1960000, "original": False},
    {"멤버": "린", "곡명": "꿈의 카니발", "조회수": 1530000, "original": False},
    {"멤버": "린", "곡명": "To X", "조회수": 5000000, "original": False},
    {"멤버": "린", "곡명": "X/Y/Z", "조회수": 5570000, "original": False},
    {"멤버": "린", "곡명": "BOW AND ARROW", "조회수": 2920000, "original": False},
    {"멤버": "린", "곡명": "Unbreakable Sphere", "조회수": 770000, "original": False},
    {"멤버": "린", "곡명": "Stand By You", "조회수": 1910000, "original": False},
    {"멤버": "린", "곡명": "만찬가", "조회수": 2450000, "original": False},
    {"멤버": "린", "곡명": "별자리가 될 수 있다면", "조회수": 2260000, "original": False},
    {"멤버": "린", "곡명": "Play", "조회수": 4610000, "original": False},
    {"멤버": "린", "곡명": "전방향 미소녀", "조회수": 1330000, "original": False},
    {"멤버": "린", "곡명": "IRIS OUT", "조회수": 2820000, "original": False},
    {"멤버": "린", "곡명": "STAY", "조회수": 4210000, "original": False},
    {"멤버": "린", "곡명": "All I Want For Christmas is you", "조회수": 2540000, "original": False},
    {"멤버": "린", "곡명": "사신", "조회수": 2720000, "original": False},
    {"멤버": "린", "곡명": "카가리비토", "조회수": 1000000, "original": False},
    {"멤버": "린", "곡명": "Alzo", "조회수": 1860000, "original": False},
    {"멤버": "린", "곡명": "Oh....", "조회수": 1510000, "original": False},
    {"멤버": "린", "곡명": "아이네 클라이네", "조회수": 1070000, "original": False},
    {"멤버": "린", "곡명": "댄스홀", "조회수": 2320000, "original": False},
    {"멤버": "린", "곡명": "물떼새", "조회수": 2150000, "original": False},
    {"멤버": "린", "곡명": "소녀레이", "조회수": 680000, "original": False},
    {"멤버": "린", "곡명": "불가행력", "조회수": 1310000, "original": False},
    {"멤버": "린", "곡명": "아 프리오리", "조회수": 1270000, "original": False},
    {"멤버": "린", "곡명": "Chocolate box(with 유니)", "조회수": 560000, "original": False},
    {"멤버": "린", "곡명": "Dynamite(with 네리사)", "조회수": 1510000, "original": False},
    {"멤버": "린", "곡명": "잿빛과 푸름(with 리코)", "조회수": 2090000, "original": False},
    {"멤버": "린", "곡명": "Work(with 나나)", "조회수": 1090000, "original": False},
    {"멤버": "린", "곡명": "쿵쿵 앞으로(with 부키)", "조회수": 630000, "original": False},
    {"멤버": "린", "곡명": "아이덴티티(with 부키)", "조회수": 2040000, "original": False},
]

# 4. 세션 상태(게임 데이터) 초기화
def init_songs():
    sorted_init = sorted(INITIAL_SONGS, key=lambda x: x["조회수"], reverse=True)
    return [dict(song, 변동=0, prev_rank_1m=i+1, initial_rank=i+1, is_trending=False, is_live=False) for i, song in enumerate(sorted_init)]

if "songs" not in st.session_state:
    st.session_state.songs = init_songs()
    st.session_state.tick = 0
    st.session_state.is_running = True
    st.session_state.recent_trending = []
    st.session_state.active_live_member = None
    st.session_state.live_timer = 0
else:
    for i, song in enumerate(st.session_state.songs):
        if "prev_rank_1m" not in song:
            song["prev_rank_1m"] = i + 1
        if "initial_rank" not in song:
            song["initial_rank"] = i + 1
        if "변동" not in song:
            song["변동"] = 0
        if "original" not in song:
            song["original"] = False
        if "is_trending" not in song:
            song["is_trending"] = False
        if "is_live" not in song:
            song["is_live"] = False

if "recent_trending" not in st.session_state:
    st.session_state.recent_trending = []
if "active_live_member" not in st.session_state:
    st.session_state.active_live_member = None
if "live_timer" not in st.session_state:
    st.session_state.live_timer = 0

# 조회수 포맷팅 함수
def format_views(views):
    man = views / 10000
    return f"{man:,.2f}만 ({views:,}회)"

# 상단 타이틀 및 컨트롤 버튼
st.title("🎵 실시간 노래 차트 시뮬레이터")

col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
with col1:
    if st.button("⏯️ 일시정지 / 재개", use_container_width=True):
        st.session_state.is_running = not st.session_state.is_running
with col2:
    if st.button("⏩ 30분 스킵", use_container_width=True):
        # 30분 = 1800초 / 3초 틱 = 600번의 틱을 한 번에 시뮬레이션
        for _ in range(600):
            st.session_state.tick += 1
            if st.session_state.tick % 20 == 0:
                current_sorted_for_snapshot = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
                snapshot_ranks = {(song["멤버"], song["곡명"]): idx + 1 for idx, song in enumerate(current_sorted_for_snapshot)}
                for song in st.session_state.songs:
                    song["prev_rank_1m"] = snapshot_ranks[(song["멤버"], song["곡명"])]
            
            for song in st.session_state.songs:
                if random.random() < 0.001:
                    inc = random.randint(10000, 200000)
                else:
                    inc = random.randint(100, 10000)
                song["조회수"] += inc
                song["변동"] = inc
        st.rerun()

with col3:
    if st.button("🔄 차트 초기화", use_container_width=True):
        st.session_state.songs = init_songs()
        st.session_state.tick = 0
        st.session_state.recent_trending = []
        st.session_state.active_live_member = None
        st.session_state.live_timer = 0
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

        # 스페셜 라이브 타이머 관리 및 랜덤 발동 (0.5% 확률로 멤버별 라이브 시작, 10틱(30초) 유지)
        if st.session_state.live_timer > 0:
            st.session_state.live_timer -= 1
            if st.session_state.live_timer == 0:
                st.session_state.active_live_member = None
        else:
            members = list(MEMBER_THEMES.keys())
            if random.random() < 0.005:  # 0.5% 확률
                st.session_state.active_live_member = random.choice(members)
                st.session_state.live_timer = 10  # 10틱 동안 지속

        # 각 곡별 조회수 증가 계산
        for song in st.session_state.songs:
            # 인급동 체크 (0.1% 확률) - 10,000 ~ 200,000 사이 증가
            if random.random() < 0.001:
                song["is_trending"] = True
                inc = random.randint(10000, 200000)
                triggered_list.append((song["곡명"], inc))
            else:
                song["is_trending"] = False
                inc = random.randint(100, 10000)
                
                # 스페셜 라이브 진행 중인 멤버의 곡이라면 1~2배(1.2배~2배) 부스트 적용
                if song["멤버"] == st.session_state.active_live_member:
                    inc = int(inc * random.uniform(1.2, 2.0))
            
            song["조회수"] += inc
            song["변동"] = inc

    st.session_state.tick += 1
    st.session_state.recent_trending = triggered_list

    # 스페셜 라이브 진행 중 상단 배너 표시
    if st.session_state.active_live_member:
        live_info = MEMBER_THEMES.get(st.session_state.active_live_member, {})
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
                margin-bottom: 10px;
                font-weight: bold;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            ">
                <span>🎤 [스페셜 라이브] <b>{live_info.get('badge', '')}</b>의 라이브 방송 진행 중! (조회수 1~2배 부스트 발동 🚀)</span>
                <span style="font-size: 0.9em; background: rgba(255,255,255,0.2); padding: 3px 8px; border-radius: 4px;">남은 시간: 약 {st.session_state.live_timer * 3}초</span>
            </div>
            """,
            unsafe_allow_html=True
        )

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
        init_rank = song.get("initial_rank", rank)
        
        # 특수 듀엣 배지 처리
        if song["곡명"] == "Dear my fairy":
            badge_html = '<span style="background: linear-gradient(135deg, #FF8DA1, #607D8B); color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.85em; font-weight: bold;">🏫히나 & 🐱마시로</span>'
            left_border_color = "#FF8DA1"
            bg_color = "#FFF5F7"
        else:
            theme = MEMBER_THEMES.get(member, {"color": "#888888", "bg_color": "#F0F0F0", "badge": member})
            # 린, 부키, 나나처럼 밝은 배경의 배지는 글자색을 어둡게 처리
            badge_text_color = "#333" if member in ["부키", "나나", "린"] else "white"
            badge_html = f'<span style="background-color: {theme["color"]}; color: {badge_text_color}; border: 1px solid #ddd; padding: 4px 10px; border-radius: 15px; font-size: 0.85em; font-weight: bold;">{theme["badge"]}</span>'
            left_border_color = theme["color"]
            bg_color = theme["bg_color"]

        # 오리지널 곡 태그
        original_tag = ' <span style="background-color: #FFD700; color: #333; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">✨ 오리지널</span>' if song.get("original", False) else ''

        # 인급동 발동 태그
        trending_tag = ' <span style="background-color: #FF4757; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">🔥 [인급동]</span>' if song.get("is_trending", False) else ''

        # 스페셜 라이브 버프 중인 곡 태그
        live_tag = ' <span style="background-color: #8E44AD; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">🎤 [라이브버프]</span>' if member == st.session_state.active_live_member else ''

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
                    <div style="font-size: 1.2em; font-weight: 800; width: 60px; text-align: center; color: #222;">
                        {rank}위 <span style="font-size: 0.75em; color: gray; font-weight: normal;">({init_rank})</span>
                    </div>
                    <div style="width: 45px; text-align: center;">
                        {rank_diff_html}
                    </div>
                    {badge_html}
                    <span style="font-size: 1.1em; font-weight: 700; color: #111;">
                        {song['곡명']}{original_tag}{trending_tag}{live_tag}
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
