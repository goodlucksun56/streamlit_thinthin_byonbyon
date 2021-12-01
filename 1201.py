

import streamlit as st
#import urllib.request, json
#import urllib.parse
#import datetime
from PIL import Image

st.title("TABITO　～中部地方編～")
st.subheader("さあ、旅へ！")

col1, col2, col3 = st.columns(3)

with col1:
    img=Image.open('hakushi.jpg')
    st.image(img,caption='',use_column_width=True)

with col2:
    img=Image.open('migi.png')
    st.image(img,caption='',use_column_width=True)
    
with col3:
    img=Image.open('tabibito.png')
    st.image(img,caption='',use_column_width=True)

st.write("あなたは中部地方の魅力をどこまで知っていますか？日本の中央部分に位置し、新潟県、富山県、石川県、福井県、長野県、岐阜県、山梨県、静岡県、愛知県と多くの県を含むエリアが中部地方です。「富士山」や「日本アルプス」など日本を代表する各地の自然で、四季折々の美しさや魅力があります。また、「合掌造り」や「松本城」、「兼六園」など歴史的価値のあるスポットが多い地域でもあります。さらに、自然が生み出す美味しい食べ物やアウトドアスポットが多くあります。魅力の溢れた中部地方に、旅へ出かけてみませんか？")
   
col1, col2, col3 = st.columns(3)

with col1:
    img=Image.open('mt.fuji.jpg')
    st.image(img,caption='富士山（山梨県）',use_column_width=True)
   
with col2:
    img=Image.open('ameharasi_kaigann.jpg')
    st.image(img,caption='雨晴海岸（富山県）',use_column_width=True)

with col3:
    img=Image.open('namaemake.jpg')
    st.image(img,caption='恋人岬（新潟県）',use_column_width=True)

st.subheader('使い方ガイド')
st.write('1.行きたい場所を選択')
st.write('2.目的を選択')
st.write('3.「検索！」ボタンをクリック')
st.write('4.「検索！」ボタンの下に表示されるURLをクリック')
st.write('5.旅でやりたいことを決めよう！')

st.subheader('旅の始まり')

where=st.selectbox(
    "行きたい場所は？",
    list(['新潟県','富山県','石川県','福井県','長野県','岐阜県','山梨県','静岡県','愛知県']))
where,'の旅をはじめよう'


want_to=st.selectbox(
    "目的は？",
    list(['食べ物','観光','アウトドア']))
want_to,'のおすすめ'

button1 = st.button('検索！')

if button1:
    if where == '新潟県' and want_to == '食べ物':
        st.subheader('新潟旅行者が選ぶ！新潟で絶対に食べるべきグルメランキングTOP10')
        st.write('https://rtrp.jp/articles/6822/')
        

    elif where == '新潟県' and want_to == '観光':
        st.subheader('現地スタッフ厳選！新潟県のおすすめ観光スポットBEST40！')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-niigata')
    
    elif where == '新潟県' and want_to == 'アウトドア':
        st.subheader('こんなこともできるんだ！新潟のアウトドアおすすめスポット20選')
        st.write('https://rtrp.jp/articles/41307/')
    
    elif  where == '富山県' and want_to == '食べ物':
        st.subheader('富山のうまい名物が食べたい！富山県の名物ご当地グルメ16選')
        st.write('https://tabijikan.jp/toyama-prefecture-specialty-foods-51434/')
    
    elif where == '富山県' and want_to == '観光':
        st.subheader('富山県のおすすめ観光スポットBEST21！現地スタッフ厳選')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-toyama')

    elif where == '富山県' and want_to == 'アウトドア':
        st.subheader('【休日は大自然と遊ぼう】富山県のおすすめアウトドアスポット')
        st.write('https://www.suv-freaks.jp/23117')     
        
    elif where == '石川県' and want_to == '食べ物':
        st.subheader('石川県のご当地グルメ　人気ランキング')
        st.write('https://gurutabi.gnavi.co.jp/i/p17/gl1/')
        
    elif where == '石川県' and want_to == '観光':
        st.subheader('現地スタッフ厳選！石川県のおすすめ観光スポットBEST23！')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-ishikawa')
        
    elif where == '石川県' and want_to == 'アウトドア':
        st.subheader('石川県のキャンプ・アウトドア特集')
        st.write('https://www.hot-ishikawa.jp/feature/camping/top')
        
    elif where == '福井県' and want_to == '食べ物':
        st.subheader('福井県のうまい名物が食べたい！福井県の名物ご当地グルメ15選')
        st.write('https://tabijikan.jp/fukui-prefecture-specialty-foods-51511/')
        
    elif where == '福井県' and want_to == '観光':
        st.subheader('現地スタッフ厳選！福井県のおすすめ観光スポットBEST21')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-fukui')
        
    elif where == '福井県' and want_to == 'アウトドア':
        st.subheader('福井県のアウトドア　アクティビティ')
        st.write('https://www.tripadvisor.jp/Attractions-g298109-Activities-c61-Fukui_Prefecture_Hokuriku_Chubu.html')
        
    elif where == '長野県' and want_to == '食べ物':
        st.subheader('長野県のご当地グルメ　人気ランキング')
        st.write('https://gurutabi.gnavi.co.jp/i/p20/gl1/')
        
    elif where == '長野県' and want_to == '観光':
        st.subheader('現地スタッフ厳選！長野県のおすすめ観光スポットBEST25！')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-nagano')
        
    elif where == '長野県' and want_to == 'アウトドア':
        st.subheader('長野県のアウトドアレジャー・体験ツアー・観光情報')
        st.write('https://sotoasobi.net/4/16')
        
    elif where == '岐阜県' and want_to == '食べ物':
        st.subheader('岐阜の旨い名物が食べたい！岐阜県のご当地グルメ15選')
        st.write('https://tabijikan.jp/gifu-prefecture-specialty-foods-49769/')
        
    elif where == '岐阜県' and want_to == '観光':
        st.subheader('岐阜県のおすすめ観光スポットBEST20！現地スタッフ厳選')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-gifu')
        
    elif where == '岐阜県' and want_to == 'アウトドア':
        st.subheader('【休日は大自然と遊ぼう】岐阜県のおすすめアウトドアスポット10選')
        st.write('https://www.suv-freaks.jp/22806')
        
    elif where == '山梨県' and want_to == '食べ物':
        st.subheader('【山梨グルメ】絶対に食べたい！おすすめ名物グルメ12選')
        st.write('https://www.jalan.net/news/article/424294/')
        
    elif where == '山梨県' and want_to == '観光':
        st.subheader('現地スタッフ厳選！山梨県のおすすめ観光スポットBEST29')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-yamanashi')
        
    elif where == '山梨県' and want_to == 'アウトドア':
        st.subheader('山梨でできるACTIVITY特集　遊び・体験おすすめスポット15選！')
        st.write('https://www.porta-y.jp/feature/activity-yamanashi')
        
    elif where == '静岡県' and want_to == '食べ物':
        st.subheader('静岡に行ったら食べたい！おすすめのご当地グルメ24選！')
        st.write('https://tabichannel.com/article/296/shizuoka_gourmet')
        
    elif where == '静岡県' and want_to == '観光':
        st.subheader('現地スタッフ厳選！静岡県のおすすめ観光スポットBEST34')
        st.write('https://travel.rakuten.co.jp/mytrip/ranking/spot-shizuoka')
        
    elif where == '静岡県' and want_to == 'アウトドア':
        st.subheader('静岡県のアウトドア')
        st.write('https://www.asoview.com/leisure/grp1/location/prf210000/')
        
    elif where == '愛知県' and want_to == '食べ物':
        st.subheader('愛知グルメ「なごやめし」')
        st.write('https://aichinavi.jp/search_foods/')
        
    elif where == '愛知県' and want_to == '観光':
        st.subheader('【愛知観光】おすすめスポット23選　名所と自然と美味しいもの')
        st.write('https://aichinavi.jp/search_foods/')
        
    elif where == '愛知県' and want_to == 'アウトドア':
        st.subheader('愛知県のアウトドア')
        st.write('https://www.asoview.com/leisure/grp1/location/prf230000/')

 