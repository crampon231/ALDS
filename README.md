# ALDS
Algorithms and Data Structures

## ソート
- 計算量と安定性
- データを保持する配列以外にメモリが必要か
- 入力データの特徴が計算量に影響するか

### 挿入ソート
ALDS_1_1_A
- 安定
- O(n^2)
- ある程度整列されたデータには高速に動作

### バブルソート
ALDS_1_2_A
- 安定
- O(n^2)
- バブルソートの交換回数は反転数または転倒数と呼ばれ、列の乱れ具合を表す

### 選択ソート
ALDS_1_2_B
- 非安定
- O(n^2)

### シェルソート
ALDS_1_3_D
- 改良挿入ソート
- 非安定
- g_{n+1} = 3g_n + 1を使うと O(n^1.25)くらい

### マージソート
ALDS1_5_B
- 安定
- O(nlogn)
- 一時的な記憶領域が必要

## データ構造
データ構造は
- データの集合
- 規則
- 操作  
からなる。

### キュー
ALDS1_3_B  
リングバッファを実装。
普段は`collections.deque`を使うのが良さそう。

### 連結リスト
ALDS1_3_C, ALDS1_3_C_2  
自分で書いたものは遅い...。

## 探索
### 線形探索
ALDS1_4_A
- O(n)
- 番兵を置くことで定数倍の高速化ができる

### 二分探索
ALDS1_4_B
- O(logn)
- 整列している場合に使用可

## 分割統治
- 与えられた問題を部分問題に分割する
- 部分問題を再帰的に解く
- 得られた部分問題の解を統合し、もとの問題を解く
