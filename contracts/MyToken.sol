// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor() ERC20("FoodParcel", "FdP") {
        _mint(msg.sender, 10000 * 10 ** decimals());
    }
}
