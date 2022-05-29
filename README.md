# Contracts for the RWA_EA projects.

## The External Adapter that this talks to
https://github.com/rogervs/RWA_EA

## 5 Minute overview of what it does
[![5 Minutes Intro Video](https://img.youtube.com/vi/VxIKy8hyWeo/0.jpg)](https://www.youtube.com/watch?v=VxIKy8hyWeo)


## Notes 
This needs to use [Operator.sol](https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.7/Operator.sol) from version v0.7 . This will not work with `Oracle.sol`.

You will also need two bridges on your node to talk to the external adapter:
1. Name: `register_audit` URL: `http://localhost:8080/register_audit/`
2. Name: `conclude_audit` URL: `http://localhost:8080/conclude_audit/`

The job files need to be added to your node:
. `register_aduit_03.toml`
. `get_data_01.toml`

You will need to set the `Operator.sol` contract address for the oracle in both scripts.

Place the jobId's in brownie-config.yaml

You will need to create `.env` file, copied from `.env.example`. All the fields need to be filled out except for etherscan, but I highly recommend you do use it.
