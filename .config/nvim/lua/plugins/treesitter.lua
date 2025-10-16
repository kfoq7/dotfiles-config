return {
  {
    "nvim-treesitter/nvim-treesitter",
    branch = "master",
    opts = {
      highlight = {
        enable = true,
      },
      ensure_installed = {
        "astro",
        "cmake",
        "cpp",
        "http",
        "go",
        "scss",
        "sql",
        "java",
        "svelte",
        -- "kotlin",
      },
    },
    config = function(_, opts)
      require("nvim-treesitter.configs").setup(opts)

      vim.filetype.add({
        extension = {
          mdx = "mdx",
        },
      })
      vim.treesitter.language.register("markdown", "mdx")
    end,
  },
  -- {
  --   "nvim-treesitter/nvim-treesitter",
  --   opts = {
  --     highlight = {
  --       enable = true,
  --     },
  --     ensure_installed = {
  --       "astro",
  --       "cmake",
  --       "cpp",
  --       "http",
  --       "go",
  --       "scss",
  --       "sql",
  --       "java",
  --       "svelte",
  --     },
  --   },
  --   config = function(_, opts)
  --     require("nvim-treesitter.config").setup(opts)
  --
  --     vim.filetype.add({
  --       extension = {
  --         mdx = "mdx",
  --       },
  --     })
  --     vim.treesitter.language.register("markdown", "mdx")
  --   end,
  -- },
}
