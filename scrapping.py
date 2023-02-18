import discum, json


with open("data.json", "r") as df:
    data = json.load(df)

bot = discum.Client(token=data["token"])

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members
def save():
 members = get_members(data["guild_id"], data["guild_channel"]) 
 memberslist = []

 for memberID in members:
    memberslist.append(memberID)
    print(memberID)

 f = open('users.txt', "a")
 for element in memberslist:
    f.write(element + '\n')
 f.close()