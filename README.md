# BabbleLab-Freestyle · 苏州乱讲实验室

**别人还在想让 AI 说人话，我们的 AI 已经开始满嘴跑火车了。**

这里是苏州乱讲实验室。我们玩乱讲 PPT、即兴表演和即兴辩论：图已经翻了，人还没想好，嘴先接上。现在把真人现场的怪念头、接话和歪理整理成一个 Skill，让你的 AI 也来坐一桌。

把你那句平平无奇的发言贴过来。它顺着原意走两步，可能会发现这句话居然还有个后门。你只想回一句，它就接一句；给它一张图、一句台词或一个辩题，也能继续往下讲。

> 沉着冷静，即使一无所知。
>
> ——乱讲实验室

## 刷新一下你的发言

你原本想说：

> 怎么还没到周五？

刷新一下：

> 周五在路上了，拎着两大袋周四，走不快。

你原本想说：

> 我家很小。

刷新一下：

> 朋友问客厅在哪，我往旁边让了半步。

再放飞一点：

> 我家没有走廊，主要靠转念。刚想去厨房，人已经到了。朋友来参观，我说慢一点，你刚才那个逗号把卧室走完了。

这些是项目原创示例。更多[原话与刷新后的对照](examples/refresh-your-lines.md)，以及[长段侃聊、英文即兴和奇想](examples/showcase.md)，可以接着看。

## 真人的脑洞，长这样

黑糖的置顶互动让大家“用下属的语气说句话”。有人申请出差报销“五个亿”，作者接：

> 你去地府出差了？

有人说“You are fired”，作者接：

> 我是火？

这是[黑糖的公开互动](https://www.xiaohongshu.com/explore/673b40cc0000000002038ac8)。我们把这种接话的转弯放进了技能。

[《小设计找妈妈》](https://www.xiaohongshu.com/explore/6ad09578000000001303f04b)借了“找妈妈”的童话，一路找审美、找预算、找一个愿意理解设计师的人。等到一句“妈妈，尾款呢？”，童话也得结账。这种能讲长一点、最后又落回具体处境的办法，技能里也有。

现场换一张图，歪理还得接着上班。[《阳澄湖水怪是真实存在的！》](https://www.xiaohongshu.com/explore/689f2c5a000000001b0337a4)把越来越不搭的动物图片接进同一套“伪装、进化”的说法；[《东方之门的航空使命》](https://www.xiaohongshu.com/explore/68a81390000000001d029937)边指图、边改解释，连新出现的“大脑”图也能接回前面。谁发布、谁发言、哪些片段已经核对，都在[现场取材记录](docs/research/field-recordings.md)里。

## 话筒递给你，想怎么玩

| 来自哪里 | 你可以拿它做什么 |
|---|---|
| 乱讲 PPT | 给一张不搭的图找歪理，把上一页说过的话圆到下一页；也能帮你出一批有得讲的题目 |
| 即兴表演 | 给角色和场景，和它一来一回地接戏；接受已经发生的事，再给对方一个新麻烦 |
| 即兴辩论 | 给立场或对方上一句，它接住那个论点抬杠，讲完把话交回来 |

群聊、开场白、吐槽、朋友间的回应和日常介绍，都能拿来试。“别太油”“冷一点”“嘴碎一点”“再野一点”“只要一句”直接说，它听得懂。

乱讲实验室的即兴辩论，说完把蓝色手柄一推，话就到了对面；现场活动的投票靠观众欢呼。这个 Skill 也得懂得轮到谁说话：接完自己这一轮，把下一句留给你。

## 把第一句递过来

```text
$babblelab-freestyle 把这句发言刷新得有趣一点，适合发群里，别写长：……
```

```text
$babblelab-freestyle 即兴接戏。你是保安，我是给月亮送外卖的人。
我说：“师傅，月亮留的门牌号怎么在你后脑勺上？”只接你这一轮。
```

```text
$babblelab-freestyle 即兴辩论。对方说：“午睡就是偷走下午的时间。”
你支持午睡，接住他这句话反驳，别写成议论文。
```

```text
$babblelab-freestyle 我刚讲完“冰箱正在向南迁徙”，下一页突然是一盆仙人掌。
帮我接过去，认真讲歪理。
```

给现成发言加趣味，原意、数字、日期和条件要留住。周五交稿，放飞以后也得是周五，不能顺嘴交给下个朝代。明确要胡说八道、编故事或表演，就可以大胆创造设定。想认真回答时说“别加戏”；英文也可以用。

## 安装

```bash
git clone https://github.com/yn-fan/BabbleLab-Freestyle.git
cd BabbleLab-Freestyle
```

Codex：

```bash
python3 tools/install.py --to ~/.agents/skills
```

Claude Code：

```bash
python3 tools/install.py --to ~/.claude/skills
```

Claude Code 用 `/babblelab-freestyle` 调用。其他支持 `SKILL.md` 的工具，可导入整个 [skills/babblelab-freestyle](skills/babblelab-freestyle) 文件夹。安装器需要 Python 3.9+；已有同名目录时会停止，不会覆盖。

不需要先装其他技能。作品由你使用的模型生成，效果会受模型和上下文影响。安装路径参考 [Codex](https://developers.openai.com/codex/skills/) 与 [Claude Code](https://code.claude.com/docs/en/skills) 官方说明。

## 这股劲儿，来自苏州

小红书 **@乱讲实验室**、**@黑糖不是黑桃** 的创作者，也是这个项目的发起人。这里的脑洞从苏州的创作和现场活动里长出来：有人递来一个念头，另一个人接住，拐了个弯，再递出去。

素材包括创作者提供的品牌原文、现场玩法，以及已经读到的公开图文、作者回复和录像画面字幕；新写的练习另有标注，见[创作者材料](docs/research/creator-materials.md)。真人说过的，认原作者；技能新编的，别往真人嘴里塞。这是一套创作说明，没有把模型重新训练成谁。

## 先看它怎么接

- [刷新发言的对照示例](examples/refresh-your-lines.md)
- [首轮八个场景的原始输出](eval/results.md)
- [接戏、抬杠和现场救场的新试用](eval/interaction-results.md)
- [设计与验证记录](docs/validation.md)

```bash
python3 -m unittest discover -s tests -v
```

检查能看出它有没有少带文件，看不出你有没有笑。先读作品；碰上讲完只剩礼貌性微笑的那种，[拿回来，我们一起改](CONTRIBUTING.md)。

## 致谢与许可

自然表达的基础来自 [BabbleLab-RenHua](https://github.com/yn-fan/BabbleLab-RenHua)，也参考了 PPT Karaoke、即兴教学及公开短回复；[完整出处](skills/babblelab-freestyle/THIRD_PARTY.md)继续保留。项目沿用 **[CC BY-NC 4.0](LICENSE)，限非商业使用**；公开源码不等于任意商用，相关权利须分别取得授权。
