def sort_games(*args, **kwargs):

    def trim_release_id(release_id):
        return '_'.join(release_id.split('_')[:-1])

    pc_games = [args[el][1] for el in range(len(args)) if args[el][0] == "pc"]
    console_game = [args[el][1] for el in range(len(args)) if args[el][0] == "console"]
    matched_pc_games = {}
    matched_console_games = {}
    for release_date, game in kwargs.items():
        if game in pc_games:

            for game_name in pc_games:
                if game_name == game:
                    matched_pc_games[game_name] = release_date
        else:
            for game_name in console_game:
                if game_name == game:
                    matched_console_games[game_name] = release_date
    sorted_pc_games = sorted(matched_pc_games.items(),key= lambda x: x[1], reverse=True)
    sorted_console_games = sorted(matched_console_games.items(), key=lambda x: x[1])
    result = ""
    if sorted_console_games:
        result += "Console Games:\n"
        for game_name, release_id in sorted_console_games:
            trimmed = trim_release_id(release_id)
            result += f">>>{trimmed}: {game_name}\n"
    if sorted_pc_games:
        result += "PC Games:\n"
        for game_name, release_id in sorted_pc_games:
            trimmed = trim_release_id(release_id)
            result += f"<<<{trimmed}: {game_name}\n"
    return result

print(sort_games(
    ("console", "Echo Dive"),
    ("pc", "Quantum Drift"),
    June_22_2025_001="Quantum Drift",
    March_15_2025_002="Echo Dive",
))




