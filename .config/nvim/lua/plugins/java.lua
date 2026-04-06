return {
  {
    "mfussenegger/nvim-jdtls",
    opts = {
      -- The command that starts the language server
      -- See: https://github.com/eclipse/eclipse.jdt.ls#running-from-the-command-line
      jdtls = {
        -- Set JVM memory limits to 4GB
        jvm_args = {
          "-Xmx4G",
          "-Xms1G",
        },
      },
    },
  },
}
