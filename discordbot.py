import discord
from discord.ext import commands
import random

buki_list = ['わかばシューター',
'もみじシューター',
'おちばシューター',
'スプラシューター',
'スプラシューターコラボ',
'スプラシューターベッチュー',
'プライムシューター',
'プライムシューターコラボ',
'プライムシューターベッチュー',
'.52ガロン',
'.52ガロンデコ',
'.52ガロンベッチュー',
'.96ガロン',
'.96ガロンデコ',
'ジェットスイーパー',
'ジェットスイーパーカスタム',
'ボールドマーカー',
'ボールドマーカーネオ',
'ボールドマーカー7',
'シャープマーカー',
'シャープマーカーネオ',
'N-ZAP85',
'N-ZAP89',
'N-ZAP83',
'プロモデラーMG',
'プロモデラーRG',
'プロモデラーPG',
'ホットブラスター',
'ホットブラスターカスタム',
'ロングブラスター',
'ロングブラスターカスタム',
'ロングブラスターネクロ',
'ラピッドブラスター',
'ラピッドブラスターデコ',
'ラピッドブラスターベッチュー',
'Rブラスターエリート',
'Rブラスターエリートデコ',
'ノヴァブラスター',
'ノヴァブラスターネオ',
'ノヴァブラスターベッチュー',
'クラッシュブラスター',
'クラッシュブラスターネオ',
'L3リールガン',
'L3リールガンD',
'L3リールガンベッチュー',
'H3リールガン',
'H3リールガンD',
'H3リールガンチェリー',
'ボトルガイザー',
'ボトルガイザーフォイル',
'スプラローラー',
'スプラローラーコラボ',
'スプラローラーベッチュー',
'カーボンローラー',
'カーボンローラーデコ',
'ヴァリアブルローラー',
'ヴァリアブルローラーフォイル',
'ダイナモローラー',
'ダイナモローラーテスラ',
'ダイナモローラーベッチュー',
'パブロ',
'パブロ・ヒュー',
'パーマネント・パブロ',
'ホクサイ',
'ホクサイ・ヒュー',
'ホクサイベッチュー',
'スプラチャージャー',
'スプラチャージャーコラボ',
'スプラチャージャーベッチュー',
'スプラスコープ',
'スプラスコープコラボ',
'スプラスコープベッチュー',
'リッター4K',
'リッター4Kカスタム',
'4Kスコープ',
'4Kスコープカスタム',
'ソイチューバー',
'ソイチューバーカスタム',
'スクイックリンα',
'スクイックリンβ',
'スクイックリンγ',
'14式竹筒銃・甲',
'14式竹筒銃・乙',
'14式竹筒銃・丙',
'バケットスロッシャー',
'バケットスロッシャーデコ',
'バケットスロッシャーソーダ',
'ヒッセン',
'ヒッセン・ヒュー',
'スクリュースロッシャー',
'スクリュースロッシャーネオ',
'スクリュースロッシャーベッチュー',
'オーバーフロッシャー',
'オーバーフロッシャーデコ',
'エクスプロッシャー',
'エクスプロッシャーカスタム',
'バレルスピナー',
'バレルスピナーデコ',
'バレルスピナーリミックス',
'スプラスピナー',
'スプラスピナーコラボ',
'スプラスピナーベッチュー',
'ハイドラント',
'ハイドラントカスタム',
'クーゲルシュライバー',
'クーゲルシュライバー・ヒュー',
'ノーチラス47',
'ノーチラス79',
'スプラマニューバー',
'スプラマニューバーコラボ',
'スプラマニューバーベッチュー',
'スパッタリー',
'スパッタリー・ヒュー',
'スパッタリークリア',
'デュアルスイーパー',
'デュアルスイーパーカスタム',
'ケルビン525',
'ケルビン525デコ',
'ケルビン525ベッチュー',
'クアッドホッパーブラック',
'クアッドホッパーホワイト',
'パラシェルター',
'パラシェルターソレーラ',
'キャンピングシェルター',
'キャンピングシェルターソレーラ',
'キャンピングシェルターカーモ',
'スパイガジェット',
'スパイガジェットソレーラ',
'スパイガジェットベッチュー']


client = commands.Bot(command_prefix='.')



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content == '武器':
        num = random.randint(0,128)
        w = buki_list[num]
        n = message.author.name
        if message.author.name == "ぱすた":
            await message.channel.send(n + 'さんはデュアルスイーパーカスタム')
        else:
            await message.channel.send(n + 'さんは' + w)



client.run('DISCORD_BOT_TOKEN')
