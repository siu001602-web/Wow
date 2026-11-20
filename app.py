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
        "color": "#9B72CF",
        "bg_color": "#F5EEFF",
        "badge": "🦄 유니"
    },
    "후야": {
        "color": "#FF6B8B",
        "bg_color": "#FFF0F4",
        "badge": "🐉 후야"
    },
    "마시로": {
        "color": "#607D8B",
        "bg_color": "#ECEFF1",
        "badge": "🐱 마시로"
    },
    "타비": {
        "color": "#2980B9",
        "bg_color": "#EAF2F8",
        "badge": "🧭 타비"
    },
    "히나": {
        "color": "#333333",
        "bg_color": "#2C3E50",
        "badge": "🏫 히나",
        "text_color": "white"
    },
    "리제": {
        "color": "#C0392B",
        "bg_color": "#FDEDEC",
        "badge": "🧛‍♀️ 리제"
    },
    "부키": {
        "color": "#F1C40F",
        "bg_color": "#FEF9E7",
        "badge": "🦊 부키"
    },
    "나나": {
        "color": "#FF8DA1",
        "bg_color": "#FFF0F3",
        "badge": "🔫 나나"
    },
    "린": {
        "color": "#BDC3C7",
        "bg_color": "#F8F9F9",
        "badge": "👗 린"
    },
    "유니버스": {
        "color": "#16A085",
        "bg_color": "#E8F8F5",
        "badge": "✨ 유니버스"
    },
    "시로": {
        "color": "#7F8C8D",
        "bg_color": "#F2F4F4",
        "badge": "🐱 시로"
    },
}

# 3. 초기 노래 데이터
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

# 4. 세션 상태 초기화
def init_songs():
    sorted_init = sorted(INITIAL_SONGS, key=lambda x: x["조회수"], reverse=True)
    return [dict(song, 변동=0, avg_growth=5000.0, prev_rank_1m=i+1, initial_rank=i+1, is_trending=False, is_live=False, buff=None, buff_timer=0) for i, song in enumerate(sorted_init)]

if "songs" not in st.session_state:
    st.session_state.songs = init_songs()
    st.session_state.tick = 0
    st.session_state.is_running = True
    st.session_state.recent_trending = []
    st.session_state.active_live_member = None
    st.session_state.live_timer = 0
    st.session_state.news_feed = ["📢 실시간 노래 차트 집계가 시작되었습니다! (성장률 중심 서바이벌 모드)"]
    st.session_state.history_1st_counts = {}
    st.session_state.eliminated_songs = []
else:
    for i, song in enumerate(st.session_state.songs):
        if "prev_rank_1m" not in song:
            song["prev_rank_1m"] = i + 1
        if "initial_rank" not in song:
            song["initial_rank"] = i + 1
        if "변동" not in song:
            song["변동"] = 0
        if "avg_growth" not in song:
            song["avg_growth"] = 5000.0
        if "original" not in song:
            song["original"] = False
        if "is_trending" not in song:
            song["is_trending"] = False
        if "is_live" not in song:
            song["is_live"] = False
        if "buff" not in song:
            song["buff"] = None
        if "buff_timer" not in song:
            song["buff_timer"] = 0

if "recent_trending" not in st.session_state:
    st.session_state.recent_trending = []
if "active_live_member" not in st.session_state:
    st.session_state.active_live_member = None
if "live_timer" not in st.session_state:
    st.session_state.live_timer = 0
if "news_feed" not in st.session_state:
    st.session_state.news_feed = ["📢 실시간 노래 차트 집계가 시작되었습니다!"]
if "history_1st_counts" not in st.session_state:
    st.session_state.history_1st_counts = {}
if "eliminated_songs" not in st.session_state:
    st.session_state.eliminated_songs = []

def add_news(msg):
    if not st.session_state.news_feed or st.session_state.news_feed[0] != msg:
        st.session_state.news_feed.insert(0, msg)
        st.session_state.news_feed = st.session_state.news_feed[:5]

def format_views(views):
    man = views / 10000
    return f"{man:,.2f}만 ({views:,}회)"

# --- 💀 순수 성장률 중심 서바이벌 탈락 로직 함수 ---
def evaluate_and_eliminate():
    if len(st.session_state.songs) <= 3:
        add_news("⚠️ 곡이 너무 적어 탈락 시스템이 일시 중지됩니다.")
        return

    # 절대적인 조회수가 아니라 '평균 성장률(avg_growth)'이 가장 낮은 순으로 정렬
    sorted_by_growth = sorted(st.session_state.songs, key=lambda x: x.get("avg_growth", 0))
    worst_song = sorted_by_growth[0]  # 성장률이 가장 처참한 곡 1곡 확정!
    
    reasons = [
        f"최근 조회수 증가 평균이 급감하며 리스너 유입 정체 (평균 증가량: {worst_song.get('avg_growth', 0):,.1f}회)",
        f"휴식기(너프) 또는 화제성 저조로 인해 팬덤 화력 및 알고리즘 추천 이탈 발생",
        f"타 곡들의 폭발적인 성장세에 밀려 독자적인 청취층 확보 실패",
        f"최근 집계 구간 동안 일일 증가량이 바닥을 치며 차트 경쟁력 상실"
    ]
    chosen_reason = random.choice(reasons)
    
    st.session_state.songs.remove(worst_song)
    st.session_state.eliminated_songs.insert(0, {
        "곡명": worst_song["곡명"],
        "멤버": worst_song["멤버"],
        "최종조회수": worst_song["조회수"],
        "평균성장률": worst_song.get("avg_growth", 0),
        "사유": chosen_reason
    })
    
    add_news(f"💀 [서바이벌 탈락] {worst_song['멤버']} '{worst_song['곡명']}' 최저 성장률 기록으로 차트 영구 퇴출!")

# --- 사이드바 설정 ---
st.sidebar.title("⚙️ 시뮬레이터 설정")
team_mode = st.sidebar.checkbox("👥 멤버별 팀전(진영 대항전) 모드 켜기", value=False)
survival_mode = st.sidebar.checkbox("💀 30분(600틱)마다 최저성장 곡 탈락 모드", value=True)

st.sidebar.markdown("---")
st.sidebar.title("💖 내 최애 곡 관리")
st.sidebar.markdown("차트에서 강조해서 볼 곡을 최대 **10개**까지 선택하세요!")

all_song_keys = [f"{song['멤버']} - {song['곡명']}" for song in st.session_state.songs]

if "favorite_songs" not in st.session_state:
    st.session_state.favorite_songs = []

selected_favorites = st.sidebar.multiselect(
    "최애 곡 선택 (최대 10개)",
    options=all_song_keys,
    default=st.session_state.favorite_songs,
    max_selections=10
)
st.session_state.favorite_songs = selected_favorites

# 상단 타이틀 및 컨트롤 버튼
st.title("🎵 실시간 노래 차트 시뮬레이터")

col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
with col1:
    if st.button("⏯️ 일시정지 / 재개", use_container_width=True):
        st.session_state.is_running = not st.session_state.is_running
with col2:
    if st.button("⏩ 30분 스킵", use_container_width=True):
        prev_top1 = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)[0]
        for _ in range(600):
            st.session_state.tick += 1
            if st.session_state.tick % 20 == 0:
                current_sorted_for_snapshot = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
                snapshot_ranks = {(song["멤버"], song["곡명"]): idx + 1 for idx, song in enumerate(current_sorted_for_snapshot)}
                for song in st.session_state.songs:
                    song["prev_rank_1m"] = snapshot_ranks[(song["멤버"], song["곡명"])]
            
            for song in st.session_state.songs:
                if song.get("buff"):
                    song["buff_timer"] -= 1
                    if song["buff_timer"] <= 0:
                        song["buff"] = None

                old_views = song["조회수"]
                inc = random.randint(100, 10000)
                if song.get("buff") == "buff":
                    inc *= 3
                elif song.get("buff") == "nerf":
                    inc //= 3
                
                song["조회수"] += inc
                song["변동"] = inc
                
                # 평균 성장률(지수 이동 평균 형태) 실시간 업데이트
                song["avg_growth"] = (song.get("avg_growth", inc) * 0.9) + (inc * 0.1)

                if old_views // 1000000 < song["조회수"] // 1000000:
                    milestone = (song["조회수"] // 1000000) * 100
                    add_news(f"🎉 [대기록] {song['멤버']} '{song['곡명']}' 조회수 {milestone:,}만 돌파!")

        if survival_mode:
            evaluate_and_eliminate()

        curr_sorted_after_skip = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
        if curr_sorted_after_skip:
            top1_key = f"{curr_sorted_after_skip[0]['멤버']} - {curr_sorted_after_skip[0]['곡명']}"
            st.session_state.history_1st_counts[top1_key] = st.session_state.history_1st_counts.get(top1_key, 0) + 600

        new_top1 = curr_sorted_after_skip[0]
        if (prev_top1["멤버"], prev_top1["곡명"]) != (new_top1["멤버"], new_top1["곡명"]):
            add_news(f"👑 [왕좌 교체] 30분 스킵 결과, {new_top1['멤버']} '{new_top1['곡명']}' 1위 등극!")
        else:
            add_news(f"⏩ 30분 스킵 완료! 현재 1위는 {new_top1['멤버']} '{new_top1['곡명']}'입니다.")
        st.rerun()

with col3:
    if st.button("🔄 차트 초기화", use_container_width=True):
        st.session_state.songs = init_songs()
        st.session_state.tick = 0
        st.session_state.recent_trending = []
        st.session_state.active_live_member = None
        st.session_state.live_timer = 0
        st.session_state.news_feed = ["📢 차트가 초기화되었습니다! 새로운 집계 시작!"]
        st.session_state.history_1st_counts = {}
        st.session_state.eliminated_songs = []
        st.rerun()

# --- 명예의 전당 및 탈락 곡 리포트 보기 영역 ---
with st.expander("🏆 [결산 리포트] 실시간 명예의 전당 및 탈락 곡 보기", expanded=False):
    st.markdown("### 🌟 시뮬레이션 히스토리 요약")
    
    current_sorted_eval = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown("#### 👑 최장기 왕좌 (1위 누적 유지)")
        if st.session_state.history_1st_counts:
            best_1st_song = max(st.session_state.history_1st_counts.items(), key=lambda x: x[1])
            st.info(f"🏆 **{best_1st_song[0]}**\n\n(약 {best_1st_song[1] * 3}초 동안 왕좌 사수)")
        else:
            if current_sorted_eval:
                st.info(f"👑 현재 1위: **{current_sorted_eval[0]['멤버']} - {current_sorted_eval[0]['곡명']}**")
            else:
                st.write("아직 기록된 데이터가 없습니다.")

    with col_h2:
        st.markdown("#### 🚀 최고 순위 급상승 (초기 대비)")
        best_climber = max(current_sorted_eval, key=lambda x: x.get("initial_rank", 1) - (current_sorted_eval.index(x) + 1))
        climber_diff = best_climber.get("initial_rank", 1) - (current_sorted_eval.index(best_climber) + 1)
        if climber_diff > 0:
            st.success(f"📈 **{best_climber['멤버']} - {best_climber['곡명']}**\n\n(초기 {best_climber.get('initial_rank')}위 ➡️ 현재 {current_sorted_eval.index(best_climber)+1}위, **+{climber_diff}계단** 상승!)")
        else:
            st.write("아직 큰 순위 변동이 없습니다.")

    st.markdown("---")
    st.markdown("#### 💀 서바이벌 탈락 곡 기록 (성장률 부진 기준)")
    if st.session_state.eliminated_songs:
        for elim in st.session_state.eliminated_songs:
            st.warning(f"❌ **[{elim['멤버']}] {elim['곡명']}** (최종 조회수: {format_views(elim['최종조회수'])} | 평균 성장률: {elim['평균성장률']:,.1f}회/틱)\n\n💡 **탈락 사유:** {elim['사유']}")
    else:
        st.write("아직 탈락한 곡이 없습니다. (서바이벌이 진행되면 여기에 기록됩니다)")

    st.markdown("---")
    st.markdown("#### 🥉 현재 생존 TOP 3 요약")
    for top_idx in range(min(3, len(current_sorted_eval))):
        ts = current_sorted_eval[top_idx]
        medals = ["🥇", "🥈", "🥉"]
        st.write(f"{medals[top_idx]} **{top_idx+1}위** | [{ts['멤버']}] {ts['곡명']} — {format_views(ts['조회수'])}")

# 5. 3초마다 자동 실행되는 실시간 차트 영역
@st.fragment(run_every=3)
def live_chart():
    triggered_list = []
    
    prev_sorted = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
    prev_top1_key = (prev_sorted[0]["멤버"], prev_sorted[0]["곡명"]) if prev_sorted else None
    
    if st.session_state.is_running and st.session_state.tick > 0:
        if survival_mode and st.session_state.tick > 0 and st.session_state.tick % 200 == 0:
            evaluate_and_eliminate()

        if st.session_state.tick % 20 == 0:
            snapshot_ranks = {(song["멤버"], song["곡명"]): idx + 1 for idx, song in enumerate(prev_sorted)}
            for song in st.session_state.songs:
                song["prev_rank_1m"] = snapshot_ranks[(song["멤버"], song["곡명"])]

        # 무작위 버프/너프 카드 이벤트 (10분 = 200틱 동안 유지)
        if random.random() < 0.03:
            target_song = random.choice(st.session_state.songs)
            if target_song.get("buff") is None:
                effect_type = random.choice(["buff", "nerf"])
                target_song["buff"] = effect_type
                target_song["buff_timer"] = 200  # 3초 * 200 = 600초 (10분)
                if effect_type == "buff":
                    add_news(f"🚀 [돌발 버프] {target_song['멤버']} '{target_song['곡명']}' 떡상 버프 발동! (10분간 조회수 3배)")
                else:
                    add_news(f"💤 [돌발 너프] {target_song['멤버']} '{target_song['곡명']}' 휴식기 너프 발동! (10분간 조회수 감소)")

        if st.session_state.live_timer > 0:
            st.session_state.live_timer -= 1
            if st.session_state.live_timer == 0:
                st.session_state.active_live_member = None
        else:
            members = list(MEMBER_THEMES.keys())
            if random.random() < 0.005:
                st.session_state.active_live_member = random.choice(members)
                st.session_state.live_timer = 10
                add_news(f"🎤 [속보] {st.session_state.active_live_member}의 스페셜 라이브가 시작되었습니다!")

        for song in st.session_state.songs:
            if song.get("buff"):
                song["buff_timer"] -= 1
                if song["buff_timer"] <= 0:
                    add_news(f"✨ [효과 종료] {song['멤버']} '{song['곡명']}' 10분간의 버프/너프 효과가 종료되었습니다.")
                    song["buff"] = None

            old_views = song["조회수"]
            if random.random() < 0.001:
                song["is_trending"] = True
                inc = random.randint(10000, 200000)
                triggered_list.append((song["곡명"], inc))
                add_news(f"🔥 [인급동] {song['멤버']} '{song['곡명']}' 인기 급상승! (+{inc:,}회)")
            else:
                song["is_trending"] = False
                inc = random.randint(100, 10000)
                
                if song.get("buff") == "buff":
                    inc *= 3
                elif song.get("buff") == "nerf":
                    inc //= 3

                if song["멤버"] == st.session_state.active_live_member:
                    inc = int(inc * random.uniform(1.2, 2.0))
            
            song["조회수"] += inc
            song["변동"] = inc
            
            # 평균 성장률 업데이트 (지수 이동 평균)
            song["avg_growth"] = (song.get("avg_growth", inc) * 0.9) + (inc * 0.1)

            if old_views // 1000000 < song["조회수"] // 1000000:
                milestone = (song["조회수"] // 1000000) * 100
                add_news(f"🎉 [경축] {song['멤버']} '{song['곡명']}' 조회수 {milestone:,}만 돌파!")

    st.session_state.tick += 1
    st.session_state.recent_trending = triggered_list

    current_sorted = sorted(st.session_state.songs, key=lambda x: x["조회수"], reverse=True)
    
    if current_sorted:
        top1_song_key = f"{current_sorted[0]['멤버']} - {current_sorted[0]['곡명']}"
        st.session_state.history_1st_counts[top1_song_key] = st.session_state.history_1st_counts.get(top1_song_key, 0) + 3

    if current_sorted and prev_top1_key and st.session_state.tick > 1:
        curr_top1 = current_sorted[0]
        if (curr_top1["멤버"], curr_top1["곡명"]) != prev_top1_key:
            add_news(f"👑 [1위 역전] {curr_top1['멤버']} '{curr_top1['곡명']}' 차트 정상 탈환!")

    # --- 📰 실시간 차트 속보 뉴스 티커 (전광판) 렌더링 ---
    ticker_items = " &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; ".join(st.session_state.news_feed)
    st.markdown(
        f"""
        <style>
        @keyframes ticker-scroll {{
            0% {{ transform: translateX(100%); }}
            100% {{ transform: translateX(-100%); }}
        }}
        .news-ticker-container {{
            background-color: #1E1E2E;
            color: #F8F8F2;
            border: 2px solid #FF4757;
            border-radius: 8px;
            padding: 8px 15px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            overflow: hidden;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        }}
        .news-ticker-badge {{
            background-color: #FF4757;
            color: white;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 5px;
            margin-right: 15px;
            white-space: nowrap;
            font-size: 0.9em;
            z-index: 2;
        }}
        .news-ticker-wrap {{
            flex: 1;
            overflow: hidden;
            white-space: nowrap;
        }}
        .news-ticker-text {{
            display: inline-block;
            font-weight: 600;
            font-size: 0.95em;
            color: #FFEAA7;
            animation: ticker-scroll 22s linear infinite;
        }}
        </style>
        <div class="news-ticker-container">
            <div class="news-ticker-badge">📰 실시간 속보</div>
            <div class="news-ticker-wrap">
                <div class="news-ticker-text">{ticker_items}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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

    # --- 팀전 모드가 켜져 있을 때 멤버별 총합 조회수 순위 표시 ---
    if team_mode:
        team_totals = {}
        for song in st.session_state.songs:
            m = song["멤버"]
            team_totals[m] = team_totals.get(m, 0) + song["조회수"]
        
        sorted_teams = sorted(team_totals.items(), key=lambda x: x[1], reverse=True)

        st.markdown("### 🏆 [진영 대항전] 멤버별 총합 조회수 순위")
        team_cols = st.columns(len(sorted_teams))
        for idx, (t_name, t_val) in enumerate(sorted_teams):
            t_theme = MEMBER_THEMES.get(t_name, {"color": "#888"})
            with team_cols[idx % len(team_cols)]:
                st.markdown(
                    f"""
                    <div style="
                        background-color: {t_theme.get('bg_color', '#f8f9fa')};
                        border: 2px solid {t_theme.get('color', '#888')};
                        padding: 10px;
                        border-radius: 8px;
                        text-align: center;
                        margin-bottom: 15px;
                    ">
                        <div style="font-weight: 800; font-size: 1.1em;">{idx+1}위 {t_name}</div>
                        <div style="font-size: 0.9em; font-weight: bold; color: #333;">{format_views(t_val)}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        st.markdown("---")

    status_text = "🟢 실시간 집계 중 (3초 갱신 / 1분 단위 순위 반영)" if st.session_state.is_running else "⏸️ 일시정지됨"
    st.caption(f"{status_text} | 생존 곡: {len(current_sorted)}곡 경쟁 중 | 경과 시간: {(st.session_state.tick - 1) * 3}초")

    for idx, song in enumerate(current_sorted):
        rank = idx + 1
        member = song["멤버"]
        song_key = f"{member} - {song['곡명']}"
        init_rank = song.get("initial_rank", rank)
        
        is_favorite = song_key in st.session_state.favorite_songs
        fav_badge = ' <span style="background-color: #E67E22; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">👑 최애</span>' if is_favorite else ''

        buff_badge = ''
        if song.get("buff") == "buff":
            remain_min = (song.get("buff_timer", 0) * 3) // 60
            remain_sec = (song.get("buff_timer", 0) * 3) % 60
            buff_badge = f' <span style="background-color: #27AE60; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">🚀 떡상중(3배, 잔여 {remain_min}분 {remain_sec}초)</span>'
        elif song.get("buff") == "nerf":
            remain_min = (song.get("buff_timer", 0) * 3) // 60
            remain_sec = (song.get("buff_timer", 0) * 3) % 60
            buff_badge = f' <span style="background-color: #7F8C8D; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">💤 휴식기(잔여 {remain_min}분 {remain_sec}초)</span>'

        if song["곡명"] == "Dear my fairy":
            badge_html = '<span style="background: linear-gradient(135deg, #FF8DA1, #607D8B); color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.85em; font-weight: bold;">🏫히나 & 🐱마시로</span>'
            left_border_color = "#FF8DA1"
            bg_color = "#FFF5F7"
            text_color = "#111"
        else:
            theme = MEMBER_THEMES.get(member, {"color": "#888888", "bg_color": "#F0F0F0", "badge": member})
            badge_text_color = "#333" if member in ["부키", "나나", "린"] else "white"
            badge_html = f'<span style="background-color: {theme["color"]}; color: {badge_text_color}; border: 1px solid #ddd; padding: 4px 10px; border-radius: 15px; font-size: 0.85em; font-weight: bold;">{theme["badge"]}</span>'
            left_border_color = theme["color"]
            bg_color = theme["bg_color"]
            text_color = "white" if member == "히나" else "#111"

        original_tag = ' <span style="background-color: #FFD700; color: #333; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">✨ 오리지널</span>' if song.get("original", False) else ''
        trending_tag = ' <span style="background-color: #FF4757; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">🔥 [인급동]</span>' if song.get("is_trending", False) else ''
        live_tag = ' <span style="background-color: #8E44AD; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75em; font-weight: bold; margin-left: 6px;">🎤 [라이브버프]</span>' if member == st.session_state.active_live_member else ''

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
        rank_num_color = "white" if member == "히나" else "#222"
        views_color = "white" if member == "히나" else "#222"

        card_border = "3px solid #F1C40F" if is_favorite else f"8px solid {left_border_color}"

        st.markdown(
            f"""
            <div style="
                display: flex;
                align-items: center;
                justify-content: space-between;
                background-color: {bg_color};
                border-left: {card_border};
                padding: 12px 20px;
                margin-bottom: 8px;
                border-radius: 8px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.08);
            ">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 1.2em; font-weight: 800; width: 60px; text-align: center; color: {rank_num_color};">
                        {rank}위 <span style="font-size: 0.75em; color: {'#aaa' if member == '히나' else 'gray'}; font-weight: normal;">({init_rank})</span>
                    </div>
                    <div style="width: 45px; text-align: center;">
                        {rank_diff_html}
                    </div>
                    {badge_html}
                    <span style="font-size: 1.1em; font-weight: 700; color: {text_color};">
                        {song['곡명']}{fav_badge}{buff_badge}{original_tag}{trending_tag}{live_tag}
                    </span>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 1.05em; font-weight: 700; color: {views_color};">
                        {format_views(song['조회수'])}
                    </div>
                    <div style="font-size: 0.8em; color: {'#F1C40F' if member == '히나' else '#E67E22'}; font-weight: 600;">
                        {inc_text}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

live_chart()
