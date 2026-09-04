#!/bin/bash

DST_DIR="/Users/yuyaaketa/.gemini/antigravity/scratch/Tier shindan eat/images"

declare -a files=(
"type_1.jpg"
"type_2.jpg"
"type_3.jpg"
"type_4.jpg"
"type_5.jpg"
"type_6.jpg"
"type_7.jpg"
"type_8.jpg"
"type_9.jpg"
"type_10.jpg"
"type_11.jpg"
"type_12.jpg"
"type_13.jpg"
"type_14.jpg"
"type_15.jpg"
"type_16.jpg"
)

declare -a prompts=(
"16-bit RPG pixel art sprite of an epic slice of pizza monster, glowing neon red and orange aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic tall frappuccino cup monster, glowing neon green and white aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic ramen bowl monster with noodles, glowing neon gold and yellow aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic Japanese rice ball onigiri monster, glowing neon cyan and blue aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic Japanese beef bowl gyudon monster, glowing neon purple and pink aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic coffee mug monster, glowing neon cyan and blue aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic piece of sushi monster, glowing neon pink and magenta aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic giant meat on a bone monster, glowing neon red and orange aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic bowl of udon noodles monster, glowing neon light blue aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic plate of curry rice monster, glowing neon red and yellow fire aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic strawberry shortcake monster, glowing neon pink and white aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic Japanese beef bowl gyudon monster wearing glasses, glowing neon green aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic soda glass monster with a straw, glowing neon rainbow aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic giant broccoli monster, glowing neon bright green aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic giant hamburger monster, glowing neon orange and yellow aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
"16-bit RPG pixel art sprite of an epic box of french fries monster, glowing neon yellow and gold aura, dark fantasy video game boss, highly detailed pixel art, solid pitch black background, masterpiece"
)

for i in "${!files[@]}"; do
    filename="${files[$i]}"
    prompt="${prompts[$i]}"
    
    encoded_prompt=$(jq -rn --arg x "$prompt" '$x|@uri')
    url="https://image.pollinations.ai/prompt/$encoded_prompt?width=512&height=512&nologo=true&seed=111"
    
    while true; do
        echo "Downloading $filename..."
        curl -sL -m 30 "$url" -o "/tmp/$filename"
        
        size=$(stat -f%z "/tmp/$filename" 2>/dev/null || stat -c%s "/tmp/$filename" 2>/dev/null)
        if [[ -z "$size" ]] || [[ "$size" -lt 1000 ]]; then
            echo "Failed for $filename (size $size), retrying in 5s..."
            sleep 5
        else
            echo "Saved $filename (size $size)"
            mv "/tmp/$filename" "$DST_DIR/$filename"
            break
        fi
    done
    sleep 2
done

echo "Done"
