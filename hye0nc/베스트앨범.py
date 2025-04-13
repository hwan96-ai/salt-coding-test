def main():
    print(
        solution(
            ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
        )
    )


def solution(genres, plays):
    genre_dict = {}
    genre_song = {}
    answer = []

    for i in range(len(genres)):
            genre = genres[i]
            play = plays[i]
            
            # 장르별 총 재생 횟수 갱신
            if genre not in genre_dict:
                genre_dict[genre] = 0
                genre_song[genre] = []
            genre_dict[genre] += play
            genre_song[genre].append((play, i))


    sorted_genres = sorted(
        genre_dict.keys(), key=lambda x: genre_dict[x], reverse=True
    )


    for genre in sorted_genres:
        sorted_songs = sorted(genre_song[genre], key=lambda x: (-x[0], x[1]))
        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][1])

    # for genre in sorted_genres:
    #     songs = genre_dict[genre]
    #     songs.sort(key=lambda x: (-x[1], x[0]))

    return answer


if __name__ == "__main__":
    main()
