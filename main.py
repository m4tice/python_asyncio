import asyncio


async def find_divisibles(inrange, div_by):
    print('finding num in range {} divisible by {}'.format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)

    print('Done with nums in range {} divisible by {}'.format(inrange, div_by))
    return located


async def main():
    div1 = asyncio.create_task(find_divisibles(508000, 34113))
    div2 = asyncio.create_task(find_divisibles(100052, 3210))
    div3 = asyncio.create_task(find_divisibles(500, 3))
    await asyncio.wait([div1, div2, div3])
    return div1, div2, div3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        pass
    finally:
        loop.close()

