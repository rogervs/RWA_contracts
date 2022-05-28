// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

import "@chainlink/contracts/src/v0.7/ChainlinkClient.sol";


import "@openzeppelin/contracts/access/Ownable.sol";

import "./MyToken.sol";

contract RWAConsumer is ChainlinkClient, Ownable {
    using Chainlink for Chainlink.Request;
    uint256 public init_result;
    address public conclude_result;

    address public recipient_address;
    uint public recipient_amount;


    address public oracle;
    bytes32 public init_audit_jobId;
    bytes32 public conclude_audit_jobId;
    // bytes32 public get_amount_jobId;
    bytes32 public byte_get_jobId;


    uint256 public fee;
    bytes public payload;

    bytes public data;
    string public image_url;

    address[] public beneficiaries;
    uint16[] public amounts;


    ERC20 public token;


    mapping(string => uint16) public bonds;

    // event DataFullfilled(bytes result);
    event DataRead(address result);

    constructor(address _oracle, bytes32 _init_audit_jobId, bytes32 _conclude_audit_jobId, bytes32 _byte_get_jobId, uint256 _fee, address _link) {
        if (_link == address(0)) {
            setPublicChainlinkToken();
        } else {
            setChainlinkToken(_link);
        }
        oracle = _oracle;
        setChainlinkToken(_link);
        setChainlinkOracle(_oracle);
        // jobId = stringToBytes32(_jobId);
        init_audit_jobId = _init_audit_jobId;
        conclude_audit_jobId = _conclude_audit_jobId;
        byte_get_jobId = _byte_get_jobId;
        fee = _fee;
        token = new MyToken();
    }

    event Sold(uint256 amount);



    function bondOf(string memory _audit) public view returns(uint16) {
        return bonds[_audit];
    }



    /**
     * Create a Chainlink request to retrieve API response, find the target
     * data, then multiply by 1000000000000000000 (to remove decimal places from data).
     */
    function initiate_audit(string memory _name, string memory _admin_jid, uint _bond) public returns (bytes32 requestId)
    {
        Chainlink.Request memory request = buildChainlinkRequest(init_audit_jobId, address(this), this.initiate_response.selector);

        request.add("name", _name);
        request.add("admin_jid", _admin_jid);
        request.addUint("bond", _bond);


        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }

    /**
     * Receive the response in the form of uint256
     */
    function initiate_response(bytes32 _requestId, uint256 _init_result) public recordChainlinkFulfillment(_requestId)
    {
        init_result = _init_result;
        // emit DataFullfilled(result);
    }


    function conclude_audit(string memory _name) public returns (bytes32 requestId)
    {
        Chainlink.Request memory request = buildChainlinkRequest(conclude_audit_jobId, address(this), this.conclude_response.selector);

        request.add("name", _name);


        // Sends the request
        return sendChainlinkRequestTo(oracle, request, fee);
    }

    function conclude_response(bytes32 _requestId, address _conclude_result) public recordChainlinkFulfillment(_requestId)
    {
        conclude_result = _conclude_result;

        emit DataRead(_conclude_result);
    }


    function setOracle(address _oracle) onlyOwner public {
        oracle = _oracle;
    }

    function set_init_audit_JobId(bytes32 _init_audit_jobId) onlyOwner public {
        init_audit_jobId = _init_audit_jobId;
    }


    function set_conclude_audit_JobId(bytes32 _conclude_audit_jobId) onlyOwner public {
        conclude_audit_jobId = _conclude_audit_jobId;
    }



    function set_byte_get_JobId(bytes32 _byte_get_jobId) onlyOwner public {
        byte_get_jobId = _byte_get_jobId;
    }

    function setFee(uint256 _fee) onlyOwner public {
        fee = _fee;
    }


    event RequestFulfilled(bytes32 indexed requestId, bytes indexed data);





    function requestBytes(string memory _name) public {
        Chainlink.Request memory request = buildChainlinkRequest(byte_get_jobId, address(this), this.fulfillBytes.selector);
        request.add("name", _name);
        sendChainlinkRequest(request, fee);
    }


    function fulfillBytes(bytes32 requestId, bytes memory bytesData) public recordChainlinkFulfillment(requestId) {
        emit RequestFulfilled(requestId, bytesData);
        data = bytesData;
    }

    function bytesToArrays() public {
        (beneficiaries, amounts) = abi.decode(data, (address[], uint16[]));
    }


    function get(uint256 amount) public {
            token.transfer(msg.sender, amount);
        }

    function run(string memory _name) public {
        bytesToArrays();
        if (beneficiaries.length > 0) {
            distributeFunds(beneficiaries, amounts);
            }

    }

    function distributeFunds(address[] memory receivers, uint16[] memory amounts) public {
        for (uint256 i = 0; i < receivers.length; i++) {
            uint256 sendAmount = amounts[i] * 1000000000000000000;
            token.transfer(payable(receivers[i]), sendAmount);
        }
    }




}
