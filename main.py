import asyncio

from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair, StarkCurveSigner
from starknet_py.contract import Contract

from decouple import config

from abi import abi

client = FullNodeClient(node_url="http://127.0.0.1:5050/rpc")

KEY_PAIR = KeyPair.from_private_key(key=config("PRIVATE_KEY"))

ACCOUNT_ADDRESS = "0x72bfc23cba2f0bc5d94fba12d487a291fd5419e350400f61da7999dc37a973d"

CONTRACT_ADDRESS = "0x2b2abe6c666bba172adeaf332c3bfff3531d69230d3dc9bb0e6bdbca5e63b1d"

account = Account(
    client=client,
    address=ACCOUNT_ADDRESS,
    key_pair=KEY_PAIR,
    chain=StarknetChainId.SEPOLIA,
)

contract = Contract(
    address=CONTRACT_ADDRESS,
    abi=abi,
    provider=account,
    cairo_version=1,
)


async def get_owner():
    (saved,) = await contract.functions["get_owner"].call()
    print(saved)


async def get_payment(payment_id):
    (saved,) = await contract.functions["get_payment"].call(payment_id)
    print(saved)


async def invoke_add_payment():
    payment_id = 5555
    receiver_address_hex = "0x11a3deccd3aa40c8d4b0412600d00efe757b0bec3e5c2870c3ce16843701e0d"
    amount = 1000

    receiver_address_felt = int(receiver_address_hex, 16)

    tx_receipt = await contract.functions["add_payment"].invoke_v1(
        payment_id,
        receiver_address_felt,
        amount,
        max_fee=int(1e16)
    )

    print(f"Transaction receipt: {tx_receipt}")


# sncast call -a 0x2b2abe6c666bba172adeaf332c3bfff3531d69230d3dc9bb0e6bdbca5e63b1d -f get_owner
asyncio.run(get_owner())

# sncast call -a 0x2b2abe6c666bba172adeaf332c3bfff3531d69230d3dc9bb0e6bdbca5e63b1d -f get_payment --calldata 1234
asyncio.run(get_payment(1234))

# sncast invoke -a 0x2b2abe6c666bba172adeaf332c3bfff3531d69230d3dc9bb0e6bdbca5e63b1d -f add_payment --calldata 5555 0x11a3deccd3aa40c8d4b0412600d00efe757b0bec3e5c2870c3ce16843701e0d 1000 --fee-token strk
asyncio.run(invoke_add_payment())


