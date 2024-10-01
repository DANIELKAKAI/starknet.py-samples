abi = [
    {
        "type": "impl",
        "name": "LetapayImpl",
        "interface_name": "smart_contracts::ILetapay"
    },
    {
        "type": "enum",
        "name": "smart_contracts::Letapay::PaymentStatus",
        "variants": [
            {
                "name": "AWAITING_TRANSFER",
                "type": "()"
            },
            {
                "name": "COMPLETE",
                "type": "()"
            }
        ]
    },
    {
        "type": "struct",
        "name": "smart_contracts::Letapay::Payment",
        "members": [
            {
                "name": "payment_id",
                "type": "core::felt252"
            },
            {
                "name": "amount",
                "type": "core::felt252"
            },
            {
                "name": "status",
                "type": "smart_contracts::Letapay::PaymentStatus"
            },
            {
                "name": "sender_address",
                "type": "core::starknet::contract_address::ContractAddress"
            },
            {
                "name": "receiver_address",
                "type": "core::starknet::contract_address::ContractAddress"
            }
        ]
    },
    {
        "type": "interface",
        "name": "smart_contracts::ILetapay",
        "items": [
            {
                "type": "function",
                "name": "add_payment",
                "inputs": [
                    {
                        "name": "payment_id",
                        "type": "core::felt252"
                    },
                    {
                        "name": "receiver_address",
                        "type": "core::starknet::contract_address::ContractAddress"
                    },
                    {
                        "name": "amount",
                        "type": "core::felt252"
                    }
                ],
                "outputs": [],
                "state_mutability": "external"
            },
            {
                "type": "function",
                "name": "get_payment",
                "inputs": [
                    {
                        "name": "payment_id",
                        "type": "core::felt252"
                    }
                ],
                "outputs": [
                    {
                        "type": "smart_contracts::Letapay::Payment"
                    }
                ],
                "state_mutability": "view"
            },
            {
                "type": "function",
                "name": "complete_payment",
                "inputs": [
                    {
                        "name": "payment_id",
                        "type": "core::felt252"
                    }
                ],
                "outputs": [],
                "state_mutability": "external"
            },
            {
                "type": "function",
                "name": "get_owner",
                "inputs": [],
                "outputs": [
                    {
                        "type": "core::starknet::contract_address::ContractAddress"
                    }
                ],
                "state_mutability": "view"
            }
        ]
    },
    {
        "type": "constructor",
        "name": "constructor",
        "inputs": []
    },
    {
        "type": "event",
        "name": "smart_contracts::Letapay::PaymentAdded",
        "kind": "struct",
        "members": [
            {
                "name": "payment_id",
                "type": "core::felt252",
                "kind": "key"
            },
            {
                "name": "amount",
                "type": "core::felt252",
                "kind": "data"
            },
            {
                "name": "sender_address",
                "type": "core::starknet::contract_address::ContractAddress",
                "kind": "data"
            },
            {
                "name": "receiver_address",
                "type": "core::starknet::contract_address::ContractAddress",
                "kind": "data"
            }
        ]
    },
    {
        "type": "event",
        "name": "smart_contracts::Letapay::PaymentCompleted",
        "kind": "struct",
        "members": [
            {
                "name": "payment_id",
                "type": "core::felt252",
                "kind": "key"
            },
            {
                "name": "amount",
                "type": "core::felt252",
                "kind": "data"
            },
            {
                "name": "sender_address",
                "type": "core::starknet::contract_address::ContractAddress",
                "kind": "data"
            },
            {
                "name": "receiver_address",
                "type": "core::starknet::contract_address::ContractAddress",
                "kind": "data"
            }
        ]
    },
    {
        "type": "event",
        "name": "smart_contracts::Letapay::Event",
        "kind": "enum",
        "variants": [
            {
                "name": "PaymentAdded",
                "type": "smart_contracts::Letapay::PaymentAdded",
                "kind": "nested"
            },
            {
                "name": "PaymentCompleted",
                "type": "smart_contracts::Letapay::PaymentCompleted",
                "kind": "nested"
            }
        ]
    }
]