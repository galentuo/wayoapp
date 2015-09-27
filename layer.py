from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
import datetime



class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(),
                                                    'read', messageProtocolEntity.getParticipant())

            # outgoingMessageProtocolEntity = TextMessageProtocolEntity(messageProtocolEntity.getBody(),
            #                                                           to = messageProtocolEntity.getFrom())

            body = messageProtocolEntity.getBody()
            sender = messageProtocolEntity.getFrom()
            timeStamp = messageProtocolEntity.getTimestamp()
            time = datetime.datetime.fromtimestamp(int(timeStamp)).strftime('%Y-%m-%d %H:%M:%S')
            sender_no = (sender.split('@'))[0]
            print "[%s] %s: %s" % (time, sender_no, body)

            self.toLower(receipt)
            # self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)