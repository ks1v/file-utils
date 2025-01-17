#!/bin/zsh

# Set the root directory
cd "$1"

# Convert timestamp from '2021-04-14-23h16m05s298' to '2021-04-14 23-06-28.675'
for file in ./**/*(DN); do if [[ $file:t =~ (.*)(([0-9]{4}-[0-9]{2}-[0-9]{2})-([0-9]{2})h([0-9]{2})m([0-9]{2})s([0-9]{3}))(.*) ]]; then mv "$file" "$file:h/${match[1]}${match[3]} ${match[4]}-${match[5]}-${match[6]}.${match[7]}${match[8]}"; fi; done

# Strip suffix
for file in ./**/*_vlc.*(DN); do mv "$file" "${file%_vlc.*}.${file##*.}"; done
for file in ./**/*_VLC.*(DN); do mv "$file" "${file%_VLC.*}.${file##*.}"; done

# Strip prefix 
for file in ./**/*(DN); do if [[ $file:t =~ ^vlcsnap-(.*)$ ]]; then mv $file $file:h/${match[1]}; fi; done
for file in ./**/*(DN); do if [[ $file:t =~ ^Screenshot_(.*)$ ]]; then mv $file $file:h/${match[1]}; fi; done
for file in ./**/*(DN); do if [[ $file:t =~ "^Screenshot from (.*)$" ]]; then mv $file $file:h/${match[1]}; fi; done

# Add prefix from parent folder name
for file in ./**/*(.); do target_dir="${file:h}"; mv "$file" "${target_dir}/${target_dir:t}_${file:t:r}.${file:e}"; done

# Find and delete junk files 
find . -type f \( -name "*~" -o -name ".*~" -o -name "*.bak" -o -name "*.tmp" -o -name "*.swp" -o -name "*.swo" -o -name "*.swn" -o -name ".DS_Store" -o -name "Thumbs.db" \) -print
find . -type f \( -name "*~" -o -name ".*~" -o -name "*.bak" -o -name "*.tmp" -o -name "*.swp" -o -name "*.swo" -o -name "*.swn" -o -name ".DS_Store" -o -name "Thumbs.db" \) -delete

#
month=7; count=0; for file in "./**/*72024-*(D)"; do new_name=${file//72024-/7 2024-}; echo "$new_name"; ((count++)); done; echo "Number of affected files: $count"
count=0; for file in **/*72004-*(D); do new_name=${file//72004-/7 2024-}; mv "$file" "$new_name"; echo "$new_name"; ((count++)); done; echo "Number of affected files: $count"

count=0; for file in **/*(D.); do if [[ $file == *72004-* ]]; then new_name=${file//72004-/7 2024-}; mv "$file" "$new_name"; ((count++)); fi; done; echo "Number of affected files: $count"
count=0; for file in **/*(D.); do if [[ $file == "*72024-*" ]]; then new_name="${file//72004-/7 2024-}"; echo "$new_name"; ((count++)); fi; done; echo "Number of affected files: $count"

count=0; find . -type f -name "*72004-*" -exec sh -c 'new_name=${0//72004-/7 2024-}; mv "$0" "$new_name"; ((count++))' {} \; -exec echo "Number of affected files: $count" \;
month=7; find . -type f -name "*$month2024-*" -exec sh -c 'new_name=${0//$month2024-/$month 2024-}; echo "$new_name";' \;

number=7; year=2024; find ./ -type f -name "*${number}${year}-*" -exec sh -c 'echo "$0"; new_name=${0//${number}${year}-/${number} ${year}-}; mv "$0" "$new_name"' {} \;
number=7; year=2024; find ./ -type f -name "*${number}${year}-*" -exec sh -c 'new_name=${0//${number}${year}-/${number} ${year}-}; echo "$new_name";' {} \;

number=7; year=2024; find ./ -type f -name "*${number}${year}-*" -exec sh -c 'new_name=${0//'"${number}${year}-"'/'"${number} ${year}-"'}; mv "$0" "$new_name"; echo "Renamed: $0 -> $new_name"' {} \;
number=7; year=2024; find ./ -type f -name "*${number}${year}-*" -exec sh -c 'new_name=${0//'"${number}${year}-"'/'"${number} ${year}-"'}; echo "$0 -> $new_name"' {} \;

