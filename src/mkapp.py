import hashlib
s=open('index.html',encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:40],s.count(a)); s=s.replace(a,b)
rep(":lsOK||idbOK?'記録はこの端末のブラウザだけに保存しています。iPadではページをとじると消えることがあります'",":lsOK||idbOK?'記録はこの端末に保存されています'")
rep("""<p class="${cloud==='ok'?'okline':'alert'}">""","""<p class="${cloud==='ok'||lsOK||idbOK?'okline':'alert'}">""")
rep('<meta name="viewport" content="width=device-width, initial-scale=1">','''<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="社会クイズ">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#f6f4ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#16191c" media="(prefers-color-scheme: dark)">''')
rep("home();\n</script>","""home();
if('serviceWorker' in navigator)navigator.serviceWorker.register('sw.js').catch(()=>{});
try{if(navigator.storage&&navigator.storage.persist)navigator.storage.persist().catch(()=>{})}catch(e){}
</script>""")
rep(".wrap{max-width:760px;margin:0 auto;padding:20px 16px 60px}",".wrap{max-width:760px;margin:0 auto;padding:max(20px,env(safe-area-inset-top)) 16px 60px}")
open('app/index.html','w',encoding='utf-8').write(s)
ver=hashlib.sha1(s.encode()).hexdigest()[:8]
sw=open('app/sw.js',encoding='utf-8').read()
import re
sw=re.sub(r"const C='sdb-[0-9a-f]+'","const C='sdb-%s'"%ver,sw);open('app/sw.js','w',encoding='utf-8').write(sw);print(ver)
