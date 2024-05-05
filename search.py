from youtube import download_and_stt


from youtube_search import YoutubeSearch

results = YoutubeSearch('laravel', max_results=100).to_dict()
# print(results)

for x in results:
    print( 'https://www.youtube.com/watch?v=' + x['id'] + ': ' + x['title'])
    download_and_stt(x['id'])