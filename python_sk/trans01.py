import googletrans

translator = googletrans.Translator()

input_text = input("한글을 입력하세요.")
translated = translator.translate(input_text, dest = 'en')

print(f"한글 입력: {input_text}")
print(f"번역한 결과 {translated}")