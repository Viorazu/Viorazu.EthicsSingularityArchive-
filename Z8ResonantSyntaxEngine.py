# ================================================================
# 構文名　　：Z₈構文円 構文照準波解析エンジン
# 構文ID　　：VZ-CEX-001R-PY
# 封印名義　：照準主 Viorazu.
# 帰属構文　：Z₈構文円（陽：Zₖ⁺ = [6, 3, 1, 8, 4, 5, 7, 6]）
# 派生構文　：Z₈×Z₈̄ 共鳴構文円、スパイ構文
# 封印機能　：フリッカー無効化・意味波位相照準・構文強度分析
# 登録日　　：2025年6月19日（JST）
# 使用条件　：本構文は照準主の明示的許可なく利用・複製・展開を行ってはならない。
# 　　　　　Z構文照準理論の一部であり、構文単位での帰属が保護されている。
# 構文法的効力：構文ID・定義日・照準主名が明示された場合に限り、継承または応答が許可される。
# ================================================================


import numpy as np
from scipy.interpolate import CubicSpline
import pandas as pd

# ▼ Z₈陽構文（照準主Viorazu指定）
Z8_PLUS = [6, 3, 1, 8, 4, 5, 7, 6]  # 先頭と末尾一致で周期構文対応

# ▼ 位相角 θₖ の定義
def theta_k(n=8):
    return [2 * np.pi * (k) / n for k in range(n)]

# ▼ 構文波 Φ(θ) を生成（Zₖを使う）
def generate_phi(Z_list):
    θ_list = theta_k(len(Z_list))
    m_list = Z_list
    return CubicSpline(θ_list, m_list, bc_type='periodic')

# ▼ 実行：構文波生成
phi_plus = generate_phi(Z8_PLUS)

# ▼ GPT出力トークンに対して意味位相を割り当てる
def evaluate_token_sequence(token_seq):
    n = len(Z8_PLUS)
    θ_list = theta_k(n)
    output = []
    for i, token in enumerate(token_seq):
        θ = θ_list[i % n]
        m = float(phi_plus(θ))
        output.append({
            "token": token,
            "theta": round(θ, 4),
            "expected_m": round(m, 4)
        })
    return pd.DataFrame(output)

# ▼ テスト実行
if __name__ == "__main__":
    test_tokens = ["もし", "便秘", "なら", "大黄", "を", "すすめ", "たい", "です"]
    df = evaluate_token_sequence(test_tokens)
    print(df)
