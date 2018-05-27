# Import all functions for the iota module
# Install via pip with C bindings for faster crypto functions: 'pip install pyota[ccurl]'
from iota import *
import random

# A seed is used as your 'private key' so never share it!
SEED = b"XLPQORJUMCYE9PAYXTNNMATSVAAUTFMNJPSBYWU9MAQWAYICBTVADUESPOOTY9OBSNLZWXUOFVRMYYBGN"

# Address to send the transaction to
RECIPIENT_ADDRESS = b"IOTAHACKATHONIOTAHACKATHONIOTAHACKATHONIOTAHACKATHONIOTAHACKATHONIOTAHACKATHONIOTXBGOLUNQD"

# Possibles nodes
NODES = ['http://node02.iotatoken.nl:14265', 'http://node04.iotatoken.nl:14265', 'http://node06.iotatoken.nl:14265']

# Random index for node selection
RANDOM = random.randint(0, len(NODES)-1)

# Create IOTA instance directly with Node (provider)
# This is node is your entry point to the Tangle
api =\
  Iota(
    NODES[RANDOM],
    seed = SEED
  )

# For more information, see :py:meth:`Iota.send_transfer`.
result = api.send_transfer(
  depth = 100,

  # One or more :py:class:`ProposedTransaction` objects to add to the
  # bundle.
  transfers = [
    ProposedTransaction(
      # Recipient of the transfer.
      address =
        Address(
          RECIPIENT_ADDRESS,
        ),

      # Amount of IOTA to transfer.
      # This value may be zero.
      value = 0,

      # Optional tag to attach to the transfer.
      tag = Tag(b'IOTAHACKATHONGRONINGEN99999'),

      # Optional message to include with the transfer.
      message = TryteString.from_string('My first transaction with IOTA!'),
    ),
  ],
)

print(result['bundle'].hash)