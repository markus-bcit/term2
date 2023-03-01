#!/bin/bash

# Define the file name to store the tasks
TASKS_FILE="tasks.txt"

# Define the date format used to store the due-by date
DATE_FORMAT="+%Y-%m-%d %H:%M:%S"

# Define the pager command to display tasks
PAGER="less"

# Define the help function
function show_help() {
  echo "Usage: $0 [-d <due-by-date>] [-t <tag>]"
  echo "  -d <due-by-date>  Display tasks due by the specified date in the format of yyyy-mm-dd hh:mm:ss"
  echo "  -t <tag>          Display tasks with the specified tag"
}

# Parse command line arguments
while getopts ":d:t:" opt; do
  case $opt in
    d)
      due_by_date="$OPTARG"
      ;;
    t)
      tag="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      show_help
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      show_help
      exit 1
      ;;
  esac
done

# Check if no argument is provided, display all tasks
if [[ $# -eq 0 ]]; then
  cat "$TASKS_FILE" | $PAGER
  exit 0
fi


# Display tasks with matching tag
if [[ -n "$tag" ]]; then
  echo grep -E "\[$tag\]" "$TASKS_FILE" | cut -f 1 | sort | uniq | $PAGER
  exit 0
fi

# Display tasks with matching due-by date
if [[ -n "$due_by_date" ]]; then
  due_by=$(date -d "$due_by_date" "$DATE_FORMAT")
  echo grep -E "\t$due_by$" "$TASKS_FILE" | cut -f 1 | sort | uniq | $PAGER
  exit 0
fi

# Show help if invalid options are provided
echo "Invalid options provided." >&2
show_help
exit 1