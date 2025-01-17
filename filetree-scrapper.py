
import os

root_dir = "/Users/ks1v/Stage/movie-screenshots"
output_file = root_dir + "/schreenshots-filetree.csv"



file_list = []
for root, dirs, files in os.walk(root_dir):
  for file in files:
  file_list.append(os.path.join(root, file))

file_list = get_all_files(root_dir)

print("Files count:", len(all_files))




# Count the total number of PNG files
total_files=$(find "$root_dir" -name "*.*" | wc -l)
current_file=0

echo "Total number of files: $total_files"

# Write the CSV header
#echo "foldername,filename,name,year,season_code_sf,season_code_ef,episode_code_ef,season_code_fn,episode_code_fn,timecode,creation_datetime,file_format" > $output_file

# Find all files recursively and process each file path
#find "$root_dir" -name "*.*" | while read file_path; do
file_path="/Users/ks1v/Stage/movie-screenshots/Кибердеревня S01 (2023)/Кибердеревня S1 (2023) E08/Kiberderevnya.s01.e08.2023.WEB-DL.2160p.SDR_00_02_48 2023-10-30 23-16-25.515.png"
file_path="/Users/ks1v/Stage/movie-screenshots/Lift (1983)/Lift (1983).mkv_00_26_45 2023-12-07 00-16-01.500.png"

type="M"
if [[ $file_path =~ "S[0-9]{2}" ]]; then 
  type="S"
fi

echo $type
echo $folders

folders=$(dirname "$file_path")
if [[ $type = "S" ]]; then
  season_dir=$(basename "$folders")
  entry_dir=$(basename "$(dirname "$folders")")
elif [[ $type = "M" ]]; then
  season_dir=""
  entry_dir=$(basename "$folders")
fi

echo $entry_dir
echo $season_dir

if [[ $entry_dir =~ "(.+)[[:space:]]\(([[:digit:]]{4})\)" ]]; then
  name_dir=$match[1]
  year_dir=$match[2]
else
  name_dir=""
  year_dir=""
fi
echo $name_dir
echo $year_dir


if [[ $season_dir =~ "([^[:space:]]+)[[:space:]]S([[:digit:]]{1,2})[[:space:]]\(([[:digit:]]{4})\).*E([[:digit:]]+)" ]]; then
  season_name=$match[1]
  season_code=$match[2]
  season_year=$match[3]
  season_episode=$match[4]
else
  season_name=""
  season_code=""
  season_year=""
  season_episode=""
fi
echo $season_name
echo $season_code
echo $season_year
echo $season_episode

file_name=$(basename "$file_path")
echo $file_name

if [[ $file_name =~ "([^[:space:]]+)[[:space:]]\(([[:digit:]]{4})\).*\.([[:alpha:]]{2,4})_([[:digit:]]{2}_[[:digit:]]{2}_[[:digit:]]{2})[[:space:]]([[:digit:]]{4}-[[:digit:]]{2}-[[:digit:]]{2}[[:space:]][[:digit:]]{2}-[[:digit:]]{2}-[[:digit:]]{2}).*\.([[:alpha:]]+)$" ]]; then
  name=$match[1] 
  year=$match[2]
  video_ext=$match[3]
  timecode=$match[4]
  datetime=$match[5]
  file_ext=$match[6]

  echo "Name: $name"
  echo "Year: $year"
  echo "Video extension: $video_ext"
  echo "Timecode: $timecode"
  echo "Datetime: $datetime"
  echo "File extension: $file_ext"
else 
  echo "No match found"
fi

#if [[ $file_name =~ "([^[:space:]]+)[[:space:]]\(([[:digit:]]{4})\).*\.([[:alpha:]]{2,4})_([[:digit:]]{2}_[[:digit:]]{2}_[[:digit:]]{2})[[:space:]]([[:digit:]]{4}-[[:digit:]]{2}-[[:digit:]]{2}[[:space:]][[:digit:]]{2}-[[:digit:]]{2}-[[:digit:]]{2}).*\.([[:alpha:]]+)$" ]]; then
if [[ $file_name =~ "^(?P<name>[^.]+)(?:\.s(?P<season>\d+))?(?:\.e(?P<episode>\d+))?(?:\.(?P<year>\d{4}))?.*_(?P<timecode>\d{2}_\d{2}_\d{2})\s(?P<datetime>\d{4}-\d{2}-\d{2}\s\d{2}-\d{2}-\d{2}(?:\.\d{3})?)\.\w+\.(?P<format>[^.]+)$" ]]; then 
  name=$match[1] 
  year=$match[2]
  video_ext=$match[3]
  timecode=$match[4]
  datetime=$match[5]
  file_ext=$match[6]

  echo "Name: $name"
  echo "Year: $year"
  echo "Video extension: $video_ext"
  echo "Timecode: $timecode"
  echo "Datetime: $datetime"
  echo "File extension: $file_ext"
else 
  echo "No match found"
fi


exit 1







  # Write the extracted information to the CSV file
  #echo "$foldername,$filename,$name,$year,$season_code_sf,$season_code_ef,$episode_code_ef,$season_code_fn,$episode_code_fn,$timecode,$creation_datetime,$file_format" >> $output_file

  # Increment the current file count
  #current_file=$((current_file + 1))
  
  # Calculate the progress percentage
  #progress=$((current_file * 100 / total_files))
  
  # Draw the progress bar
#  echo -ne "$name ($year)"
#  echo -ne "Processing files: [$(printf '%*s' $progress | tr ' ' '#')$(printf '%*s' $((100 - progress)) | tr ' ' '.')] $progress% ($current_file of $total_files)\r\r"
#done

#echo ""
#echo "END"


