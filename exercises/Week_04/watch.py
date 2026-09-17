import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(
        r'<iframe[^>]*src=["\']https?://(?:www\.)?youtube\.com/embed/([^"\']+)["\']',
        s
    )

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    return None

if __name__ == "__main__":
    main()


"""
<iframe ensures the URL belongs to an iframe.
[^>]* allows other attributes before src.
https?:// accepts both http:// and https://.
(?:www\.)? makes www. optional.
([^"\']+) captures the YouTube video ID.
match.group(1) retrieves that captured ID.

example <iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>
"""