if status is-interactive
    # Commands to run in interactive sessions can go here
end

alias g git
alias vim nvim
alias ll "eza -l --git --color=always --icons=always --sort=extension"
alias la "eza -la --git --color=always --icons=always --sort=extension"

starship init fish | source
# alias dev "cd ~/Dev/"
