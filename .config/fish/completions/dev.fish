# Helper function to get project names
function __dev_projects
    set -l projects_dir ~/Dev
    for d in $projects_dir/*/
        if test -d "$d"
            basename "$d"
        end
    end
end

# complete -c dev -n "count (commandline -o) = 1" -a "(__dev_projects)" -d "Project Directory"
complete -c dev -n "count (commandline -o) = 1" -f -a "(__dev_projects)" -d "Project Directory"
