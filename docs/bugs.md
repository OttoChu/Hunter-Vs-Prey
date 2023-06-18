# Bugs

*Here are the bugs found in the project.*

1. ***Fog of War doesn't work with Teleporter ability.***
    
    - When the Teleporter ability is used, the teleport map is not covered by fog.
    - It should still be covered by fog.
    - This is because the fog is only applied when printing in *print_game_state*, not the teleport map.
    - This can be fixed by applying the fog to the teleport map as well.
    - If the user tries to teleport to a tile that is covered by fog, the game should stop the user from teleporting to that tile and remove the ability charge.
    - This can be fixed by checking if the tile is covered by fog before teleporting to it.
