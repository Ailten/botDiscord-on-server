
from classFolder.functionality.AddSubRoleFromReaction import AddSubRoleFromReaction

class AddRoleFromReaction(AddSubRoleFromReaction):

    def __init__(self, bot, messageKey: str, roleKey :str, channelKey :str, guildKey="Ailten", emojiName="✅"):

        super().__init__(bot, messageKey, roleKey, channelKey, guildKey, emojiName)

        # can't trigger the event remove.
        self.isUseOnEvent.remove("on_raw_reaction_remove")