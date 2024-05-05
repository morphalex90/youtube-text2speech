from youtube_search import YoutubeSearch

results = YoutubeSearch('laravel', max_results=10).to_dict()
# print(results)

for x in results:
  print( 'https://www.youtube.com/watch?v=' + x['id'] + ': ' + x['title'])