'''
this is a prototype and is still under development
'''

import minescript as m
import pickaxe, pickaxe_list, shovel, shovel_list, axe, axe_list, sword, swords_list


inv = m.player_inventory()
mob = m.player_get_targeted_entity()
mob_id = str(mob)


if any(word in mob_id for word in sword.mobs) and not any(word in mob_id for word in sword.allowed_mobs):
    m.echo("hostile mob detected.")

    best_sword = None
    swd_slot = None
    for swd in swords_list.swords:
        for stack in inv:
            if stack.item == swd:
                best_sword = swd
                swd_slot = stack.slot
                break
        if best_sword is not None:
            break

    if best_sword is not None:
        m.echo(f"Best sword: {best_sword} is in slot {swd_slot}")
        m.player_inventory_select_slot(swd_slot)
    else:
        m.echo("no sword in hotbar")

else:
    m.echo("no hostile mob detected.")


block = m.player_get_targeted_block()
block_id = str(block)

m.echo(block_id)
if any(word in block_id for word in pickaxe.blocks):
    m.echo("match1")

    best_pickaxe = None
    pic_slot = None
    for pic in pickaxe_list.pickaxes:
        for stack in inv:
            if stack.item == pic:
                best_sword = pic
                pic_slot = stack.slot
                break
        if best_pickaxe is not None:
            break
    if best_pickaxe is not None:
        m.echo(f"Best pickaxe: {best_pickaxe} is in slot {pic_slot}")
        m.player_inventory_select_slot(pic_slot)
    else:
        m.echo("no pickaxe in hotbar")

elif any(word in block_id for word in shovel.blocks):
    m.echo("match2")

    best_shovel = None
    shov_slot = None
    for shov in shovel_list.shovels:
        for stack in inv:
            if stack.item == shov:
                best_shovel = shov
                shov_slot = stack.slot
                break
        if best_shovel is not None:
            break
    if best_shovel is not None:
        m.echo(f"Best pickaxe: {best_shovel} is in slot {shov_slot}")
        m.player_inventory_select_slot(shov_slot)
    else:
        m.echo("no shovel in hotbar")

elif any(word in block_id for word in axe.blocks):
    m.echo("match3")

    best_axe = None
    axe_slot = None
    for axe in axe_list.axes:
        for stack in inv:
            if stack.item == axe:
                best_axe = axe
                axe_slot = stack.slot
                break
        if best_axe is not None:
            break
    if best_axe is not None:
        m.echo(f"Best pickaxe: {best_axe} is in slot {axe_slot}")
        m.player_inventory_select_slot(axe_slot)
    else:
        m.echo("no axe in hotbar")
else:
    m.echo("no match")

