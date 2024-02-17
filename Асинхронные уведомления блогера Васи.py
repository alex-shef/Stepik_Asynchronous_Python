import asyncio


async def publish_post(text):
    """
    Корутина для публикации поста в блоге.
    """
    await asyncio.sleep(1)
    print(f"Пост опубликован: {text}")
    return f"Пост опубликован: {text}"


async def notify_subscribers(subscribers):
    """
    Корутина для отправки уведомления каждому подписчику.
    """
    notifications = [f"Уведомление отправлено {subscriber}" for subscriber in subscribers]
    await asyncio.gather(*[asyncio.sleep(1) for _ in subscribers])
    for notification in notifications:
        print(notification)


async def main():
    """
    Основная функция программы.
    """
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]

    # Создание и запуск задачи публикации поста
    publish_task = asyncio.create_task(publish_post(post_text))
    await publish_task

    # Создание и запуск задачи отправки уведомлений подписчикам
    notify_task = asyncio.create_task(notify_subscribers(subscribers))
    await notify_task


asyncio.run(main())
