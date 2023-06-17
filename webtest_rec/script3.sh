for file in data/*.csv; do
    d=$(basename "$file" .csv)
    s=0
    while IFS=',' read -r _ _ num; do
        s=$((s + num*8/10))
    done < "$file"
    echo "$d: $s"
done

# for file in data/*.csv; do
#     d=$(basename "$file" .csv)
#     s=0
#     while IFS=',' read -r _ _ num; do
#         s=$((s + num))
#     done < "$file"
#     S=$((S + s * 8 / 10))
# done

# echo "$d: $S"