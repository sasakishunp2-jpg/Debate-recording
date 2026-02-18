import csv

def search_by_category():
    # ユーザーから探したいカテゴリーを入力してもらう
    target = input("検索したいカテゴリーを入力してください (例: Economy): ").strip()
    
    found = False
    print(f"\n--- 「{target}」の検索結果 ---")

    try:
        # ステップ1で作ったファイルを読み込む
        with open('debate_data.csv', mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                # row[1]がカテゴリー、row[0]が動画ID
                video_id = row[0]
                category = row[1]
                
                # 入力された文字が含まれているかチェック（大文字小文字を区別しない）
                if target.lower() in category.lower():
                    print(f"URL: https://www.youtube.com/watch?v={video_id}")
                    found = True
        
        if not found:
            print("該当する動画は見つかりませんでした。")
            
    except FileNotFoundError:
        print("エラー: debate_data.csv が見つかりません。")

if __name__ == "__main__":
    search_by_category()
