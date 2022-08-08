from brownie import SimpleCollectible
from scripts.helpful_scripts import get_account, OPENSEA_URL

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri)
    tx.wait(1)
    print(
        f"you can view the nft at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("please wait up to 20 minutes and then click on refresh metadata button")
    return simple_collectible


def main():
    deploy_and_create()
