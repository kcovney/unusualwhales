from atproto import Client
import datetime

def fetch_user_posts(handle: str, limit: int = 15):
    client = Client()

    # 🔑 Login with your Bluesky handle + app password
    client.login("kcovney.bsky.social", "2doe-snqo-tuts-dfxx")

    # Get profile info
    profile = client.app.bsky.actor.get_profile(params={"actor": handle})
    did = profile.did

    # Get the user’s feed
    resp = client.app.bsky.feed.get_author_feed(params={
        "actor": handle,
        "limit": limit
    })

    posts = resp.feed
    return posts

def print_posts_reverse_chronological(posts):
    def parse_time(item):
        return datetime.datetime.fromisoformat(item.post.record.created_at.rstrip("Z"))
    posts_sorted = sorted(posts, key=parse_time, reverse=True)
    for p in posts_sorted:
        created = p.post.record.created_at
        text = getattr(p.post.record, "text", "")
        print(f"{created} — {text}")

def main():
    handle = "unusualwhales.bsky.social"
    posts = fetch_user_posts(handle, limit=15)
    print_posts_reverse_chronological(posts)

if __name__ == "__main__":
    main()
