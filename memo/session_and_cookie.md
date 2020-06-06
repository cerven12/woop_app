# Cookieとは
ブラウザに用意されたデータの**保存場所**
サーバから操作することができる

*郵便ポストのようなもの*

# Sessionとは
ユーザがあるサイトにアクセスしたときの、一連の行動。
ある程度間を開けた場合は、新しいSessionとしてカウントする。

*服屋に入った客は一点一点洋服を手にとって見る。  
このとき手にとった服の数はn着。Sessionとしては1。  
次の日に同じ人が来店した場合は、Sessionが合計で2となる。*

# SessionIDとは
特定の個人であることを証明する情報のこと。

*免許証・保険証・社員証など(SessionIDはこれらより有効期限が短いが...)*

サーバから交付されたSessionIDをブラウザのCookieやLocalStrageなどに保存しておき、WEBサービスにアクセスする毎にSessionIDを提示する。

# Session管理とは
SessionIDを用いてユーザがWEBサービスを連続的に利用できるようにすること。

*毎回ログイン処理しててはたまらない。*
*服屋では普通、客は1セッションで数着を手
に取るが、WEBサービスではSession管理をしないと、1着取るたびに店をでなければならない。*

# VueでSession管理することについて
### Q.皆、なぜLocalStrageやCookieでSessionIDを保存するのか？Vuexに保存すればよいのでは？
A. Vuexはブラウザをリロードするとリセットされてしまいうとのこと。Vuexの情報をLocalStrageやCookieに保存できる`vuex-persistedstate`がある。
-[Vue.jsのセッション管理について stackoverflow](https://stackoverflow.com/questions/45384172/best-practice-for-storing-auth-tokens-in-vuejs)

# Vue.jsにおけるとりあえずの結論と実装方法
### 利用する認証方法と保存先
#### 認証方法
JWT認証
#### 保存先
httponlyフラグのついたCookie

### 実装方法
#### Backend-Django側
#### Frontend-Vue.js側


