# Contracts for the RWA_EA projects.

This needs to use [Operator.sol](https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.7/Operator.sol) from version v0.7 . This will not work with `Oracle.sol`.

You will also need two bridges on your node to talk to the external adapter:
1. Name: `register_audit` URL: `http://localhost:8080/register_audit/`
2. Name: `conclude_audit` URL: `http://localhost:8080/conclude_audit/`
