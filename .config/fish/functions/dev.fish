# Jump into dev or prjects
function dev
    set -l projects_dir ~/Dev

    if test (count $argv) -eq 0
        cd $projects_dir
    else
        set -l target_dir "$projects_dir/$argv[1]"
        if test -d "$target_dir"
            cd "$target_dir"
        else
            # Not a valid directory, print an error
            echo (set_color red)"Error: Directory not found: $target_dir"(set_color normal)
            return 1 # Indicate failure
        end
    end
end
