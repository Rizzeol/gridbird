// Import the IOTA library.
// Install with this command: 'npm install iota.lib.js'
var IOTA = require('iota.lib.js');

// List of possible nodes
var nodes = ['http://node02.iotatoken.nl:14265', 'http://node04.iotatoken.nl:14265', 'http://node06.iotatoken.nl:14265'];

// Random index for node selection
var random = Math.floor(Math.random() * nodes.length);

// Create IOTA instance directly with Node (provider)
// This is node is your entry point to the Tangle
var iota = new IOTA({
    'provider': nodes[random]
});

// A seed is used as your 'private key' so never share it!
const seed = '9YTPIWYMNCQ9HQVCOPUSEUEJQNHDPMFZGSJDIIILSBTDHFTPXIOUOGAPAEIE9TIGHRONRPDGLJOPMSGFX'; // KEEP IT SECURE!!

// Create a message to attach to your transaction
// and convert it to Trytes (data format used by IOTA)
let message = 'Test 1';
let messageTrytes = iota.utils.toTrytes(message);

// The receiving address (Harm's wallet!)
let address = 'STTENJJESAEJBMTNFJSFN9TUSQDLHTKGPFKLFSALUCU9YOUKTFUXJBDBDILOHTPCRMRVCLXYLFGOCXFPXYXGSRJTCC';

// Construct the transfer bundle with address, 
// value (amount of IOTA), a tag and a message
var transfer = [{
    'address': address,
    'value': 10,
	'tag': 'IOTAHACKATHONGRONINGEN',
	'message': messageTrytes,
}];

// Send transfer to the Tangle. Depending on the Node config of the connected Node
// you also do the PoW at this point. The magic numbers can stay there for the Mainnet
iota.api.sendTransfer(seed, 9, 14, transfer, function(e, bundle) {
    if (e) throw e;
    console.log("Successfully sent your transfer: ", bundle);
});



