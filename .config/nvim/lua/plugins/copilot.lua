return {
  {
    "CopilotC-Nvim/CopilotChat.nvim",
    dependencies = {
      { "nvim-lua/plenary.nvim", branch = "master" },
    },
    build = "make tiktoken",
    opts = {
      model = "claude-sonnet-4.5",
      auto_insert_mode = false,
      headless = false,
      clear_chat_on_new_prompt = false,
      history_path = vim.fn.stdpath("data") .. "/copilotchat_history",
    },
    keys = {
      { "<leader>ach", "<cmd>CopilotChatLoad<cr>", desc = "Load Chat History" },
      { "<leader>acs", "<cmd>CopilotChatSave<cr>", desc = "Save Chat History" },
    },
  },
}
