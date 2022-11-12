from bot.help_command import commands_list as cmd_list

separate = '-' * 30


def send_full_help_list() -> str:
    message_returned = 'Full help list:\n'
    for command in cmd_list.commands_list.keys():
        message_returned += f'{separate}\n/{command}\n{cmd_list.commands_list[command]["description"]}\n'
        if cmd_list.commands_list[command]["arguments"] != 'none':
            message_returned += f'{cmd_list.commands_list[command]["arguments"]}\n'
    message_returned += '\n\nSupport: https://discord.gg/23mrnTkTX4'
    return message_returned
