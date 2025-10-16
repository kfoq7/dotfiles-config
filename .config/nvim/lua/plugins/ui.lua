return {
  {
    "folke/noice.nvim",
    opts = function(_, opts)
      table.insert(opts.routes, {
        filter = {
          event = "notify",
          find = "No information avaiable",
        },
        opts = { skip = true },
      })

      opts.presets.lsp_doc_border = true
    end,
  },

  -- statusline
  {
    "rcarriga/nvim-notify",
    opts = {
      timeout = 10000,
    },
  },
}
