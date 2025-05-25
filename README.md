# HTBランクアップ計算機 (HTB Rank Up Calculator)

Hack The Box (HTB) の現在の所有状況から、次のランクに到達するために必要なマシン・チャレンジの追加所有数の組み合わせを計算・表示するPythonスクリプトです。HTBのランクシステムと所有率の計算式に基づいて動作します。

## ✨ 特徴

* 現在のシステム、ユーザー、チャレンジ所有数をインタラクティブに入力
* 現在の所有率とHTBランクを自動で計算・表示
* 次の目標ランクと、そのランクに到達するための「追加システム所有数」「追加ユーザー所有数」「追加チャレンジ所有数」の組み合わせを表形式で提示
* 浮動小数点演算の誤差を考慮した計算（`math.isclose`、微調整用`epsilon`使用）

## 📝 動作環境

* Python 3.6 以上 (f-string, `math.isclose` のため)
* `colorama` ライブラリ

## 🛠️ セットアップ

 **リポジトリをクローンまたはダウンロードします。**

```bash
git clone https://github.com/namahano/HTB-Rank-Checker.git
cd HTB-Rank-Checker
pip install -r requirements.txt
```

## 🚀 使い方

1.  以下のコマンドを実行してスクリプトを起動します。
    ```bash
    python3 htb-rank-checker.py
    ```

2.  プロンプトが表示されるので、指示に従って現在の所有数を入力します。
    * 現在のアクティブシステム所有数 (例: `10`)
    * 現在のアクティブユーザー所有数 (例: `8`)
    * 現在のアクティブチャレンジ所有数 (例: `50`)

3.  入力後、現在の状況（所有率、ランク）と、次のランクに到達するための組み合わせ例が表示されます。

## 💡 計算の仕組みについて (補足)

このスクリプトで使用している所有率の計算式やランクの閾値は、Hack The Box プラットフォームで公開されている情報に基づいています。

[Hack The Box - Introduction Guide](https://help.hackthebox.com/en/articles/5185158-introduction-to-hack-the-box)

* **所有率計算式:**
    ```
    (ActiveSystemOwns + (ActiveUserOwns / 2) + (ActiveChallengeOwns / 10)) / (activeMachines + (activeMachines / 2) + (activeChallenges / 10)) * 100
    ```
* **ランクと閾値:**
    * Noob: >= 0%
    * Script Kiddie: > 5%
    * Hacker: > 20%
    * Pro Hacker: > 45%
    * Elite Hacker: > 70%
    * Guru: > 90%
    * Omniscient: = 100%

スクリプト内では、これらの情報を元に、次のランクに必要な分子の増加量を算出し、それに基づいてマシンの追加所有数（システム、ユーザー）とチャレンジの追加所有数の組み合わせを探索しています。

## ℹ️ 注意点

* このスクリプトは、Hack The Box によって提供された情報に基づいていますが、公式ツールではありません。計算結果はあくまで目安としてご利用ください。
* HTB側の仕様変更（アクティブマシン/チャレンジ数の変更、計算式の変更など）があった場合、スクリプトの定数（主に `htb_config.py` 内）を更新する必要がある場合があります。
