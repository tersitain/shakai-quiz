import json,sys
P="北海道 青森県 岩手県 宮城県 秋田県 山形県 福島県 茨城県 栃木県 群馬県 埼玉県 千葉県 東京都 神奈川県 新潟県 富山県 石川県 福井県 山梨県 長野県 岐阜県 静岡県 愛知県 三重県 滋賀県 京都府 大阪府 兵庫県 奈良県 和歌山県 鳥取県 島根県 岡山県 広島県 山口県 徳島県 香川県 愛媛県 高知県 福岡県 佐賀県 長崎県 熊本県 大分県 宮崎県 鹿児島県 沖縄県".split()
pools={"P":P,
"T":"択捉島 南鳥島 沖ノ鳥島 与那国島".split(),
"R":"信濃川 利根川 石狩川 天塩川 北上川 阿武隈川 最上川 木曽川 天竜川 阿賀野川".split(),
"L":"琵琶湖 霞ヶ浦 サロマ湖 猪苗代湖 中海 田沢湖 中禅寺湖".split(),
"I":"択捉島 国後島 沖縄島 佐渡島 奄美大島 対馬 淡路島".split(),
"M":"大雪山（旭岳） 燧ヶ岳 日光白根山 富士山 八経ヶ岳 大山 石鎚山 宮之浦岳".split(),
"Y":"札幌 金沢 長野 岡山 東京 高知 熊本 那覇".split(),
"S":"横浜市 大阪市 名古屋市 札幌市 福岡市 川崎市 神戸市 京都市 さいたま市 広島市 仙台市".split(),
"G":"釧路 銚子 焼津 境 石巻 松浦 長崎 枕崎".split(),
"K":"京浜工業地帯 中京工業地帯 阪神工業地帯 北九州工業地帯 関東内陸工業地域 京葉工業地域 東海工業地域 瀬戸内工業地域".split(),
"H":"成田国際空港 東京港 名古屋港 横浜港 神戸港 関西国際空港 大阪港 千葉港 川崎港 清水港".split(),
"N":"アメリカ カナダ 中国 韓国 インドネシア マレーシア タイ ベトナム サウジアラビア ロシア イギリス フランス ドイツ イタリア オーストラリア ブラジル".split()}
units=[];err=0
G={"J":"時事問題（2026年のニュース）","N":"年表","H":"歴史","C":"公民"}
# 年号の選択肢プールは @Yn の答えから自動でつくる
for ln in open('q.txt',encoding='utf-8').read().splitlines():
    f=ln.split('|')
    if len(f)==3 and f[2][0]=='@' and len(f[2])>2 and f[2]!='@ORDER': pools.setdefault(f[2][1:],[]); f[1] in pools[f[2][1:]] or pools[f[2][1:]].append(f[1])
for ln in open('q.txt',encoding='utf-8').read().splitlines():
    if not ln.strip(): continue
    if ln[0]=='#':
        i,t=ln[1:].split('|');units.append({"t":t,"q":[],"g":G.get(i[0],"地理データバンク")});continue
    f=ln.split('|')
    if len(f)!=3: print("BAD",ln);err=1;continue
    q,a,d=f
    if d=='@ORDER':
        its=[]
        for p in a.split('>'):
            s=p.split(':'); its.append([s[0],float(s[1]),s[2] if len(s)>2 else s[1]+'年'])
        ks=[x[1] for x in its]
        if ks!=sorted(ks) or len(set(ks))!=len(ks) or not 3<=len(its)<=5: print("ORDER",ln);err=1
        units[-1]["q"].append([q,' → '.join('%s（%s）'%(x[0],x[2]) for x in its),d,[[x[0],x[2]] for x in its]]);continue
    if d[0]=='@':
        if a not in pools[d[1:]]: print("NOPOOL",ln);err=1
    else:
        ds=d.split(';')
        if len(ds)!=3 or a in ds or len(set(ds))!=3: print("DIST",ln);err=1
        d=ds
    units[-1]["q"].append([q,a,d])
for k,v in pools.items():
    if len(v)<4 or len(set(v))!=len(v): print('POOL',k,len(v));err=1
print({k:len(v) for k,v in pools.items() if len(k)>1})
print([ (u["t"],len(u["q"])) for u in units], sum(len(u["q"]) for u in units))
if err: sys.exit(1)
html=open('tpl.html',encoding='utf-8').read().replace('/*DATA*/','const POOLS='+json.dumps(pools,ensure_ascii=False)+';const UNITS='+json.dumps(units,ensure_ascii=False)+';')
open('index.html','w',encoding='utf-8').write(html)
